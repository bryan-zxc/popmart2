# l20drv_store_product_mix

- **Row count**: 423
- **Primary key**: (store_key, category)
- **SQL script**: [l20drv_store_product_mix.sql](../../analysis/l20drv_store_product_mix.sql)

## Key Notes

- Category-level breakdown for each store
- INNER JOIN (only stores with actual 2020-2021 sales)
- Shows which categories drive each store's revenue
- 423 rows = varying category mix per store (not all stores sell all categories)
- Used for identifying dominant category per store in insights table

## Purpose

Enables product mix analysis to understand what categories drive performance at each store location.
