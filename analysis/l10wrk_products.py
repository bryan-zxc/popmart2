"""Ingest Products.csv into l10wrk_products table."""
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
# Note: Unit Cost/Price have $ symbols, commas (thousand separators), and trailing spaces
conn.execute(f"""
    CREATE OR REPLACE TABLE l10wrk_products AS
    SELECT
        CAST("ProductKey" AS INTEGER) AS product_key,
        "Product Name" AS product_name,
        "Brand" AS brand,
        "Color" AS color,
        CAST(TRIM(REPLACE(REPLACE("Unit Cost USD", '$', ''), ',', '')) AS DOUBLE) AS unit_cost_usd,
        CAST(TRIM(REPLACE(REPLACE("Unit Price USD", '$', ''), ',', '')) AS DOUBLE) AS unit_price_usd,
        "SubcategoryKey" AS subcategory_key,
        "Subcategory" AS subcategory,
        "CategoryKey" AS category_key,
        "Category" AS category
    FROM read_csv_auto('{data_dir}/Products.csv')
""")

# Verify the table
row_count = conn.execute("SELECT COUNT(*) FROM l10wrk_products").fetchone()[0]
col_count = conn.execute("SELECT COUNT(*) FROM information_schema.columns WHERE table_name = 'l10wrk_products'").fetchone()[0]

print(f"✓ Table l10wrk_products created successfully")
print(f"  Rows ingested: {row_count:,}")
print(f"  Columns: {col_count}")

# Show sample
print("\nSample rows:")
sample = conn.execute("SELECT * FROM l10wrk_products LIMIT 3").fetchall()
for row in sample:
    print(f"  {row}")

# Show brand distribution
print("\nBrand distribution:")
brand_dist = conn.execute("""
    SELECT brand, COUNT(*) as count
    FROM l10wrk_products
    GROUP BY brand
    ORDER BY count DESC
""").fetchall()
for brand, count in brand_dist:
    print(f"  {brand}: {count:,}")

# Show category distribution
print("\nCategory distribution:")
cat_dist = conn.execute("""
    SELECT category, COUNT(*) as count
    FROM l10wrk_products
    GROUP BY category
    ORDER BY count DESC
""").fetchall()
for category, count in cat_dist:
    print(f"  {category}: {count:,}")

# Verify price parsing worked
print("\nPrice statistics:")
price_stats = conn.execute("""
    SELECT
        MIN(unit_cost_usd) as min_cost,
        MAX(unit_cost_usd) as max_cost,
        AVG(unit_cost_usd) as avg_cost,
        MIN(unit_price_usd) as min_price,
        MAX(unit_price_usd) as max_price,
        AVG(unit_price_usd) as avg_price
    FROM l10wrk_products
""").fetchone()
print(f"  Cost:  ${price_stats[0]:.2f} - ${price_stats[1]:.2f} (avg ${price_stats[2]:.2f})")
print(f"  Price: ${price_stats[3]:.2f} - ${price_stats[4]:.2f} (avg ${price_stats[5]:.2f})")

conn.close()
