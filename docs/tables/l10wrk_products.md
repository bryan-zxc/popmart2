# l10wrk_products

- **Row count**: 2,517
- **Ingestion script**: [l10wrk_products.py](../../analysis/l10wrk_products.py)

## Key Notes

- Each row represents a unique product (product_key and product_name are both unique)
- Source file had currency formatting ($ symbols, comma thousand separators) - cleaned during ingestion
- 11 brands, 8 categories, 32 subcategories
- Prices range from $0.95 to $3,199.99 with average $356.83
- Most common colors: Black (602), White (505), Silver (417)

## Columns

### product_key (INTEGER) — Categorical
- 2,517 distinct values
- Unique (no duplicates)
- Nulls: 0

### product_name (VARCHAR) — Categorical
- 2,517 distinct values
- Unique (no duplicates)
- Nulls: 0

### brand (VARCHAR) — Categorical
- 11 distinct values
- Top 3: Contoso (710), Fabrikam (267), Litware (264)
- Nulls: 0

### color (VARCHAR) — Categorical
- 16 distinct values
- Top 3: Black (602), White (505), Silver (417)
- Nulls: 0

### unit_cost_usd (DOUBLE) — Numeric
- Min: 0.48 | Max: 1060.22 | Avg: 147.66
- Nulls: 0

### unit_price_usd (DOUBLE) — Numeric
- Min: 0.95 | Max: 3199.99 | Avg: 356.83
- Nulls: 0

### subcategory_key (VARCHAR) — Categorical
- 32 distinct values
- Top 3: 0308 (201), 0806 (158), 0702 (120)
- Nulls: 0

### subcategory (VARCHAR) — Categorical
- 32 distinct values
- Top 3: Computers Accessories (201), Lamps (158), Download Games (120)
- Nulls: 0

### category_key (VARCHAR) — Categorical
- 8 distinct values: 08 (661), 03 (606), 04 (372), 05 (285), 02 (222), 07 (166), 01 (115), 06 (90)
- Nulls: 0

### category (VARCHAR) — Categorical
- 8 distinct values: Home Appliances (661), Computers (606), Cameras and camcorders (372), Cell phones (285), TV and Video (222), Games and Toys (166), Audio (115), Music, Movies and Audio Books (90)
- Nulls: 0
