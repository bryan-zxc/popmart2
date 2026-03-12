"""Extract data from DuckDB for the presentation."""

import json
from pathlib import Path
import duckdb

# Get database path from manifest
manifest = json.loads(Path(".team-agent/manifest.json").read_text())
project_id = manifest["project_id"]
db_path = f"/data/projects/{project_id}/databases/data.duckdb"

con = duckdb.connect(db_path, read_only=True)

# Category profitability
categories = con.execute("""
    SELECT
        category,
        SUM(product_count) as products,
        SUM(revenue_usd) as revenue,
        SUM(margin_usd) as margin,
        SUM(margin_usd) / NULLIF(SUM(revenue_usd), 0) * 100 as margin_pct
    FROM l30exp_category_profitability
    GROUP BY category
    ORDER BY margin DESC
""").fetchdf().to_dict('records')

# Top subcategories
top_subcats = con.execute("""
    SELECT subcategory, category, margin_usd, revenue_usd
    FROM l30exp_category_profitability
    ORDER BY margin_usd DESC
    LIMIT 5
""").fetchdf().to_dict('records')

# Bottom subcategories
bottom_subcats = con.execute("""
    SELECT subcategory, category, margin_usd, revenue_usd, product_count
    FROM l30exp_category_profitability
    ORDER BY margin_usd ASC
    LIMIT 5
""").fetchdf().to_dict('records')

# Discontinuation candidates
discontinue = con.execute("""
    SELECT product_name, category, subcategory, margin_usd, revenue_usd
    FROM l30exp_product_profitability
    WHERE profitability_status != 'No Sales'
    ORDER BY margin_usd ASC
    LIMIT 20
""").fetchdf().to_dict('records')

# Store performance overview
store_overview = con.execute("""
    SELECT
        store_type,
        COUNT(*) as stores,
        SUM(revenue_usd) as revenue,
        SUM(margin_usd) as margin
    FROM l30exp_store_ranking
    GROUP BY store_type
    ORDER BY revenue DESC
""").fetchdf().to_dict('records')

# Top stores
top_stores = con.execute("""
    SELECT store_key, country, state, revenue_usd, margin_usd, square_meters,
           revenue_usd / NULLIF(square_meters, 0) as revenue_per_sqm
    FROM l30exp_store_ranking
    WHERE store_type = 'Physical'
    ORDER BY revenue_usd DESC
    LIMIT 10
""").fetchdf().to_dict('records')

# Bottom stores
bottom_stores = con.execute("""
    SELECT store_key, country, state, revenue_usd, margin_usd, square_meters,
           revenue_usd / NULLIF(square_meters, 0) as revenue_per_sqm
    FROM l30exp_store_ranking
    WHERE store_type = 'Physical'
    ORDER BY revenue_usd ASC
    LIMIT 10
""").fetchdf().to_dict('records')

# Top performer insights
top_insights = con.execute("""
    SELECT store_key, country, state, dominant_category
    FROM l30exp_store_insights
    WHERE performance_group = 'Top 10'
    ORDER BY revenue_usd DESC
""").fetchdf().to_dict('records')

# Overall stats
overall = con.execute("""
    SELECT
        SUM(revenue_usd) as total_revenue,
        SUM(margin_usd) as total_margin,
        COUNT(DISTINCT store_key) as total_stores,
        SUM(margin_usd) / NULLIF(SUM(revenue_usd), 0) * 100 as overall_margin_pct
    FROM l30exp_store_ranking
""").fetchdf().to_dict('records')[0]

con.close()

# Write to JSON
data = {
    'overall': overall,
    'categories': categories,
    'top_subcats': top_subcats,
    'bottom_subcats': bottom_subcats,
    'discontinue': discontinue,
    'store_overview': store_overview,
    'top_stores': top_stores,
    'bottom_stores': bottom_stores,
    'top_insights': top_insights
}

Path('reporting/data.json').write_text(json.dumps(data, indent=2, default=str))
print("Data extracted to reporting/data.json")
