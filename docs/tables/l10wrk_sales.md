# l10wrk_sales

- **Row count**: 62,884
- **Ingestion script**: [l10wrk_sales.py](../../analysis/l10wrk_sales.py)

## Key Notes

- Each row represents a single transaction line item
- 26,326 distinct orders with an average of 2.16 line items per order
- 79.1% of records have null delivery_date (likely in-store pickup or online orders)
- Data spans 2016-01-01 to 2021-02-20 (5+ years)
- Sales grew from 6,905 rows in 2016 to peak of 21,611 in 2019, then declined
- StoreKey=0 represents 13,165 rows (20.9% - likely online/direct sales)

## Columns

### order_number (INTEGER) — Categorical
- 26,326 distinct values
- Top 3: 405002 (7), 406001 (7), 420003 (7)
- Nulls: 0

### line_item (INTEGER) — Numeric
- Min: 1 | Max: 7 | Avg: 2.16
- Nulls: 0

### order_date (DATE) — Date
- Range: 2016-01-01 to 2021-02-20
- Nulls: 0 | Special dates (1900/9999): 0
- Count by year: 2016 (6,905), 2017 (7,942), 2018 (14,188), 2019 (21,611), 2020 (11,026), 2021 (1,212)

### delivery_date (DATE) — Date
- Range: 2016-01-06 to 2021-02-27
- Nulls: 49,719 | Special dates (1900/9999): 0
- Count by year: 2016 (1,083), 2017 (1,570), 2018 (2,907), 2019 (4,648), 2020 (2,595), 2021 (362)

### customer_key (INTEGER) — Categorical
- 11,887 distinct values
- Top 3: 723572 (36), 1925694 (32), 1579183 (32)
- Nulls: 0

### store_key (INTEGER) — Categorical
- 58 distinct values
- Top 3: 0 (13,165), 9 (1,577), 50 (1,519)
- Nulls: 0

### product_key (INTEGER) — Categorical
- 2,492 distinct values
- Top 3: 423 (162), 434 (158), 446 (158)
- Nulls: 0

### quantity (INTEGER) — Numeric
- Min: 1 | Max: 10 | Avg: 3.14
- Nulls: 0

### currency_code (VARCHAR) — Categorical
- 5 distinct values: USD (33,767), EUR (12,621), GBP (8,140), CAD (5,415), AUD (2,941)
- Nulls: 0
