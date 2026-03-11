"""Ingest Exchange_Rates.csv into l10wrk_exchange_rates table."""
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
    CREATE OR REPLACE TABLE l10wrk_exchange_rates AS
    SELECT
        CAST("Date" AS DATE) AS date,
        "Currency" AS currency,
        CAST("Exchange" AS DOUBLE) AS exchange_rate
    FROM read_csv_auto('{data_dir}/Exchange_Rates.csv')
""")

# Verify the table
row_count = conn.execute("SELECT COUNT(*) FROM l10wrk_exchange_rates").fetchone()[0]
col_count = conn.execute("SELECT COUNT(*) FROM information_schema.columns WHERE table_name = 'l10wrk_exchange_rates'").fetchone()[0]

print(f"✓ Table l10wrk_exchange_rates created successfully")
print(f"  Rows ingested: {row_count:,}")
print(f"  Columns: {col_count}")

# Show sample
print("\nSample rows:")
sample = conn.execute("SELECT * FROM l10wrk_exchange_rates ORDER BY date, currency LIMIT 10").fetchall()
for row in sample:
    print(f"  {row}")

# Show currency list
print("\nCurrencies:")
currencies = conn.execute("SELECT DISTINCT currency FROM l10wrk_exchange_rates ORDER BY currency").fetchall()
for (currency,) in currencies:
    print(f"  {currency}")

# Show date range
date_range = conn.execute("SELECT MIN(date), MAX(date) FROM l10wrk_exchange_rates").fetchone()
print(f"\nDate range: {date_range[0]} to {date_range[1]}")

# Check USD is always 1.0
usd_check = conn.execute("SELECT MIN(exchange_rate), MAX(exchange_rate) FROM l10wrk_exchange_rates WHERE currency = 'USD'").fetchone()
print(f"USD exchange rate: {usd_check[0]} to {usd_check[1]} (should be 1.0)")

conn.close()
