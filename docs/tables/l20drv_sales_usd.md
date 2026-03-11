# l20drv_sales_usd

- **Row count**: 12,238
- **Primary key**: (order_number, line_item)
- **SQL script**: [l20drv_sales_usd.sql](../../analysis/l20drv_sales_usd.sql)

## Key Notes

- Foundation table for all 2020-2021 analysis
- Filters sales to 2020-01-01 through 2021-02-20 (14 months)
- Converts all transactions to USD using daily exchange rates
- Joins sales → products → exchange_rates
- Includes product attributes (brand, category, subcategory) for downstream aggregations
- Calculates revenue_usd, cost_usd, and margin_usd per line item

## Purpose

Normalizes multi-currency sales data into a single USD basis for consistent profitability analysis across all products and stores.
