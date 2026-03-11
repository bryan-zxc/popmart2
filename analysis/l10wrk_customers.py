"""Ingest Customers.csv into l10wrk_customers table.

ENCODING HANDLING:
The source file contains non-UTF8 characters (German city names with umlauts).
We read the file as bytes, decode with latin-1, and write a properly encoded temp file.
"""
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

# Read the file with latin-1 encoding and write UTF-8 version
source_file = f"{data_dir}/Customers.csv"
temp_file = "/tmp/customers_utf8.csv"

print("Converting encoding from latin-1 to UTF-8...")
with open(source_file, 'r', encoding='latin-1') as f_in:
    with open(temp_file, 'w', encoding='utf-8') as f_out:
        f_out.write(f_in.read())

print("✓ Converted file to UTF-8")

# Now ingest the UTF-8 file
conn.execute(f"""
    CREATE OR REPLACE TABLE l10wrk_customers AS
    SELECT
        CAST("CustomerKey" AS INTEGER) AS customer_key,
        "Gender" AS gender,
        "Name" AS name,
        "City" AS city,
        "State Code" AS state_code,
        "State" AS state,
        "Zip Code" AS zip_code,
        "Country" AS country,
        "Continent" AS continent,
        CAST("Birthday" AS DATE) AS birthday
    FROM read_csv_auto('{temp_file}')
""")

# Verify the table
row_count = conn.execute("SELECT COUNT(*) FROM l10wrk_customers").fetchone()[0]
col_count = conn.execute("SELECT COUNT(*) FROM information_schema.columns WHERE table_name = 'l10wrk_customers'").fetchone()[0]

print(f"✓ Table l10wrk_customers created successfully")
print(f"  Rows ingested: {row_count:,}")
print(f"  Columns: {col_count}")

# Verify we got all 15,266 rows
expected = 15266
if row_count == expected:
    print(f"  ✓ All {expected:,} rows ingested")
else:
    print(f"  ⚠ Expected {expected:,} rows, got {row_count:,}")

# Show sample
print("\nSample rows:")
sample = conn.execute("SELECT * FROM l10wrk_customers LIMIT 3").fetchall()
for row in sample:
    print(f"  {row}")

# Verify German records were included
print("\nCountry distribution:")
country_dist = conn.execute("""
    SELECT country, COUNT(*) as count
    FROM l10wrk_customers
    GROUP BY country
    ORDER BY count DESC
    LIMIT 10
""").fetchall()
for country, count in country_dist:
    print(f"  {country}: {count:,}")

# Show German city examples to verify encoding worked
print("\nSample German cities (verifying encoding):")
german_cities = conn.execute("""
    SELECT DISTINCT city
    FROM l10wrk_customers
    WHERE country = 'Germany'
    LIMIT 5
""").fetchall()
for (city,) in german_cities:
    print(f"  {city}")

conn.close()

# Clean up temp file
import os
os.remove(temp_file)
print(f"\n✓ Cleaned up temporary file")
