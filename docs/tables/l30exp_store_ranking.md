# l30exp_store_ranking

- **Row count**: 67
- **Primary key**: store_key
- **SQL script**: [l30exp_store_ranking.sql](../../analysis/l30exp_store_ranking.sql)

## Key Notes

- Complete store performance ranking for Initiative 2
- All 67 stores (66 physical + 1 online)
- Includes revenue_rank, margin_rank, efficiency_rank
- Store_type classification (Online/Physical) for filtering
- Years_active_in_period calculated for age-based analysis
- Efficiency_rank uses NULLS LAST to handle online store

## Purpose

Primary deliverable for Store Performance initiative - enables identification of top/bottom performers and comparison of online vs physical channels.
