# l20drv_product_performance

- **Row count**: 2,517
- **Primary key**: product_key
- **SQL script**: [l20drv_product_performance.sql](../../analysis/l20drv_product_performance.sql)

## Key Notes

- Aggregates 2020-2021 sales by product
- LEFT JOIN ensures all products appear even with zero sales in analysis period
- Includes order count, units sold, revenue, cost, margin in USD
- Calculates margin percentage with NULLIF to prevent division by zero
- Foundation for product profitability analysis (Initiative 1)

## Purpose

Provides product-level performance metrics for identifying profitable vs unprofitable products in the 2020-2021 period.
