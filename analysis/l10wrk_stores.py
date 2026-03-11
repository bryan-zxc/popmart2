"""Ingest Stores.csv into l10wrk_stores table."""
import duckdb
import json
from pathlib import Path

# Load project paths from manifest
manifest = json.loads(Path(".team-agent/manifest.json").read_text())
project_id = manifest["project_id"]
data_dir = f"/data/projects/{project_id}/repo/data/raw"
db_path = f"/data/projects/{project_id}/databases/data.duckdb"

# Connect to DuckDB
conn = duckdb.connect(db_path)

# Ingest with column renaming and type casting
conn.execute(f"""
    CREATE OR REPLACE TABLE l10wrk_stores AS
    SELECT
        CAST("StoreKey" AS INTEGER) AS store_key,
        "Country" AS country,
        "State" AS state,
        CAST("Square Meters" AS INTEGER) AS square_meters,
        CAST("Open Date" AS DATE) AS open_date
    FROM read_csv_auto('{data_dir}/Stores.csv')
""")

# Verify the table
row_count = conn.execute("SELECT COUNT(*) FROM l10wrk_stores").fetchone()[0]
col_count = conn.execute("SELECT COUNT(*) FROM information_schema.columns WHERE table_name = 'l10wrk_stores'").fetchone()[0]

print(f"✓ Table l10wrk_stores created successfully")
print(f"  Rows ingested: {row_count:,}")
print(f"  Columns: {col_count}")

# Show sample
print("\nSample rows:")
sample = conn.execute("SELECT * FROM l10wrk_stores LIMIT 5").fetchall()
for row in sample:
    print(f"  {row}")

# Check for online store
online = conn.execute("SELECT * FROM l10wrk_stores WHERE store_key = 0").fetchone()
if online:
    print(f"\n✓ Online store record found: {online}")

# Show country distribution
print("\nCountry distribution:")
country_dist = conn.execute("""
    SELECT country, COUNT(*) as count
    FROM l10wrk_stores
    GROUP BY country
    ORDER BY count DESC
""").fetchall()
for country, count in country_dist:
    print(f"  {country}: {count:,}")

# Check null square_meters
null_sqm = conn.execute("SELECT COUNT(*) FROM l10wrk_stores WHERE square_meters IS NULL").fetchone()[0]
if null_sqm > 0:
    print(f"\n⚠ {null_sqm} store(s) with null square_meters (likely online store)")

conn.close()
