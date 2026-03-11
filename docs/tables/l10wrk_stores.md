# l10wrk_stores

- **Row count**: 67
- **Ingestion script**: [l10wrk_stores.py](../../analysis/l10wrk_stores.py)

## Key Notes

- Each row represents a physical store location (plus one online store record)
- Store Key 0 represents "Online" with null square_meters
- 66 physical stores across 7 countries
- Store openings span 2005-2019
- Physical store sizes range from 245 to 2,105 square meters

## Columns

### store_key (INTEGER) — Categorical
- 67 distinct values (0-66)
- Unique (no duplicates)
- Nulls: 0
- Note: 0 = Online store

### country (VARCHAR) — Categorical
- 8 distinct values
- United States (24), Germany (9), France (7), United Kingdom (7), Australia (6), Netherlands (5), Canada (5), Italy (3), Online (1)
- Nulls: 0

### state (VARCHAR) — Categorical
- 67 distinct values (one per store)
- Unique (no duplicates)
- Nulls: 0

### square_meters (INTEGER) — Numeric
- Min: 245 | Max: 2105 | Avg: ~1400
- Nulls: 1 (Online store)

### open_date (DATE) — Date
- Range: 2005-03-04 to 2019-03-05
- Nulls: 0
