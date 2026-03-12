"""Extract key insights from analysis tables for presentation."""

import json
from pathlib import Path
import duckdb

# Get database path from manifest
manifest = json.loads(Path(".team-agent/manifest.json").read_text())
project_id = manifest["project_id"]
db_path = f"/data/projects/{project_id}/databases/data.duckdb"

con = duckdb.connect(db_path, read_only=True)

print("=" * 80)
print("INITIATIVE 1: PRODUCT LINE RATIONALISATION")
print("=" * 80)

# Category profitability overview
print("\n--- Category Profitability Summary ---")
category_summary = con.execute("""
    SELECT
        category,
        COUNT(*) as subcategories,
        SUM(product_count) as products,
        SUM(revenue_usd) as revenue,
        SUM(margin_usd) as margin,
        SUM(margin_usd) / NULLIF(SUM(revenue_usd), 0) * 100 as margin_pct
    FROM l30exp_category_profitability
    GROUP BY category
    ORDER BY margin DESC
""").fetchall()

for cat in category_summary:
    print(f"{cat[0]:30s} | Products: {cat[2]:4.0f} | Revenue: ${cat[3]:12,.0f} | Margin: ${cat[4]:12,.0f} ({cat[5]:5.1f}%)")

# Top performing subcategories
print("\n--- Top 5 Most Profitable Subcategories ---")
top_subcats = con.execute("""
    SELECT subcategory, category, margin_usd, revenue_usd,
           margin_usd / NULLIF(revenue_usd, 0) * 100 as margin_pct
    FROM l30exp_category_profitability
    ORDER BY margin_usd DESC
    LIMIT 5
""").fetchall()

for sc in top_subcats:
    print(f"{sc[0]:30s} ({sc[1]:20s}) | ${sc[2]:10,.0f} ({sc[4]:5.1f}%)")

# Bottom performing subcategories
print("\n--- Bottom 5 Least Profitable Subcategories ---")
bottom_subcats = con.execute("""
    SELECT subcategory, category, margin_usd, revenue_usd, product_count,
           margin_usd / NULLIF(revenue_usd, 0) * 100 as margin_pct
    FROM l30exp_category_profitability
    ORDER BY margin_usd ASC
    LIMIT 5
""").fetchall()

for sc in bottom_subcats:
    print(f"{sc[0]:30s} ({sc[1]:20s}) | ${sc[2]:10,.0f} ({sc[5]:5.1f}%) | {sc[4]} products")

# Product discontinuation candidates
print("\n--- Products Recommended for Discontinuation ---")
print("(Bottom 50 by margin with sales in 2020-2021)")
discontinue = con.execute("""
    SELECT product_name, category, subcategory, margin_usd, revenue_usd, units_sold,
           margin_usd / NULLIF(revenue_usd, 0) * 100 as margin_pct
    FROM l30exp_product_profitability
    WHERE profitability_status != 'No Sales'
    ORDER BY margin_usd ASC
    LIMIT 50
""").fetchall()

print(f"\nTotal candidates: {len(discontinue)}")
for i, prod in enumerate(discontinue[:10], 1):
    print(f"{i:2d}. {prod[0][:50]:50s} | {prod[1]:15s} | ${prod[3]:8,.0f} ({prod[6]:6.1f}%)")
print(f"... and {len(discontinue) - 10} more")

# Products with no sales
print("\n--- Products with No Sales (2020-2021) ---")
no_sales = con.execute("""
    SELECT COUNT(*), category
    FROM l30exp_product_profitability
    WHERE profitability_status = 'No Sales'
    GROUP BY category
    ORDER BY COUNT(*) DESC
""").fetchall()

total_no_sales = sum(row[0] for row in no_sales)
print(f"Total products with no sales: {total_no_sales}")
for cat in no_sales[:5]:
    print(f"  {cat[1]:30s}: {cat[0]:3d} products")

print("\n" + "=" * 80)
print("INITIATIVE 2: STORE PERFORMANCE & BEST PRACTICE")
print("=" * 80)

# Overall store performance
print("\n--- Store Performance Overview ---")
store_overview = con.execute("""
    SELECT
        store_type,
        COUNT(*) as stores,
        SUM(revenue_usd) as revenue,
        SUM(margin_usd) as margin,
        AVG(margin_usd / NULLIF(revenue_usd, 0) * 100) as avg_margin_pct
    FROM l30exp_store_ranking
    GROUP BY store_type
    ORDER BY revenue DESC
""").fetchall()

for st in store_overview:
    print(f"{st[0]:10s} | Stores: {st[1]:3d} | Revenue: ${st[2]:14,.0f} | Margin: ${st[3]:14,.0f} ({st[4]:5.1f}%)")

# Top 10 performing stores
print("\n--- Top 10 Performing Stores (by revenue) ---")
top_stores = con.execute("""
    SELECT store_key, country, state, revenue_usd, margin_usd,
           margin_usd / NULLIF(revenue_usd, 0) * 100 as margin_pct,
           square_meters, revenue_usd / NULLIF(square_meters, 0) as revenue_per_sqm
    FROM l30exp_store_ranking
    WHERE store_type = 'Physical'
    ORDER BY revenue_usd DESC
    LIMIT 10
""").fetchall()

for store in top_stores:
    location = f"{store[1]} - {store[2]}" if store[2] else store[1]
    print(f"Store {store[0]:3d} | {location:40s} | ${store[3]:10,.0f} | ${store[7]:6,.0f}/sqm | {store[5]:5.1f}% margin")

# Bottom 10 performing stores
print("\n--- Bottom 10 Performing Stores (by revenue) ---")
bottom_stores = con.execute("""
    SELECT store_key, country, state, revenue_usd, margin_usd,
           margin_usd / NULLIF(revenue_usd, 0) * 100 as margin_pct,
           square_meters, revenue_usd / NULLIF(square_meters, 0) as revenue_per_sqm,
           years_active_in_period
    FROM l30exp_store_ranking
    WHERE store_type = 'Physical'
    ORDER BY revenue_usd ASC
    LIMIT 10
""").fetchall()

for store in bottom_stores:
    location = f"{store[1]} - {store[2]}" if store[2] else store[1]
    print(f"Store {store[0]:3d} | {location:40s} | ${store[3]:10,.0f} | ${store[7]:6,.0f}/sqm | {store[8]:.1f}y active")

# Store insights - what drives success
print("\n--- Success Drivers: Dominant Categories at Top Performers ---")
top_insights = con.execute("""
    SELECT store_key, country, state, dominant_category, revenue_usd
    FROM l30exp_store_insights
    WHERE performance_group = 'Top 10'
    ORDER BY revenue_usd DESC
""").fetchall()

category_counts = {}
for store in top_insights:
    cat = store[3]
    category_counts[cat] = category_counts.get(cat, 0) + 1
    location = f"{store[1]} - {store[2]}" if store[2] else store[1]
    print(f"Store {store[0]:3d} | {location:40s} | {store[3]:30s}")

print(f"\nDominant category distribution in top performers:")
for cat, count in sorted(category_counts.items(), key=lambda x: x[1], reverse=True):
    print(f"  {cat:30s}: {count} stores")

# Store insights - bottom performer analysis
print("\n--- Bottom Performers: Online Conversion Candidates ---")
bottom_insights = con.execute("""
    SELECT store_key, country, state, dominant_category,
           revenue_usd, margin_usd, square_meters,
           revenue_usd / NULLIF(square_meters, 0) as revenue_per_sqm
    FROM l30exp_store_insights
    WHERE performance_group = 'Bottom 10'
    ORDER BY revenue_usd ASC
""").fetchall()

for store in bottom_insights:
    location = f"{store[1]} - {store[2]}" if store[2] else store[1]
    print(f"Store {store[0]:3d} | {location:40s} | ${store[4]:10,.0f} | ${store[7]:6,.0f}/sqm")

print("\n" + "=" * 80)

con.close()
