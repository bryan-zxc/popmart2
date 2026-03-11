# l20drv_store_performance

- **Row count**: 67
- **Primary key**: store_key
- **SQL script**: [l20drv_store_performance.sql](../../analysis/l20drv_store_performance.sql)

## Key Notes

- Aggregates 2020-2021 sales by store (all 67 stores including online)
- LEFT JOIN ensures stores with no sales in period still appear
- Calculates revenue, cost, margin, avg order value
- Includes revenue_per_sqm efficiency metric (null for online store)
- Foundation for store performance analysis (Initiative 2)

## Purpose

Provides store-level performance metrics for ranking stores and identifying top/bottom performers.
