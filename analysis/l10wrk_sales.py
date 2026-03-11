"""Ingest Sales.csv into l10wrk_sales table."""
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
    CREATE OR REPLACE TABLE l10wrk_sales AS
    SELECT
        CAST("Order Number" AS INTEGER) AS order_number,
        CAST("Line Item" AS INTEGER) AS line_item,
        CAST("Order Date" AS DATE) AS order_date,
        CAST("Delivery Date" AS DATE) AS delivery_date,
        CAST("CustomerKey" AS INTEGER) AS customer_key,
        CAST("StoreKey" AS INTEGER) AS store_key,
        CAST("ProductKey" AS INTEGER) AS product_key,
        CAST("Quantity" AS INTEGER) AS quantity,
        "Currency Code" AS currency_code
    FROM read_csv_auto('{data_dir}/Sales.csv')
""")

# Verify the table
row_count = conn.execute("SELECT COUNT(*) FROM l10wrk_sales").fetchone()[0]
col_count = conn.execute("SELECT COUNT(*) FROM information_schema.columns WHERE table_name = 'l10wrk_sales'").fetchone()[0]

print(f"✓ Table l10wrk_sales created successfully")
print(f"  Rows ingested: {row_count:,}")
print(f"  Columns: {col_count}")

# Show sample
print("\nSample rows:")
sample = conn.execute("SELECT * FROM l10wrk_sales LIMIT 3").fetchall()
for row in sample:
    print(f"  {row}")

# Check null delivery dates
null_delivery = conn.execute("SELECT COUNT(*) FROM l10wrk_sales WHERE delivery_date IS NULL").fetchone()[0]
print(f"\nDelivery date nulls: {null_delivery:,} ({100*null_delivery/row_count:.1f}%)")

# Show currency distribution
print("\nCurrency distribution:")
currency_dist = conn.execute("""
    SELECT currency_code, COUNT(*) as count
    FROM l10wrk_sales
    GROUP BY currency_code
    ORDER BY count DESC
""").fetchall()
for currency, count in currency_dist:
    print(f"  {currency}: {count:,}")

conn.close()
