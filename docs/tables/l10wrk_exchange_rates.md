# l10wrk_exchange_rates

- **Row count**: 11,215
- **Ingestion script**: [l10wrk_exchange_rates.py](../../analysis/l10wrk_exchange_rates.py)

## Key Notes

- Daily exchange rates from USD to 5 currencies
- Date range: 2015-01-01 to 2021-02-20 (matches sales data period)
- USD exchange rate is always 1.0 (base currency)
- 5 currencies × ~2,243 days = 11,215 rows

## Columns

### date (DATE) — Date
- Range: 2015-01-01 to 2021-02-20
- Nulls: 0
- 2,243 distinct dates

### currency (VARCHAR) — Categorical
- 5 distinct values: AUD, CAD, EUR, GBP, USD
- Nulls: 0

### exchange_rate (DOUBLE) — Numeric
- Min: 0.64 | Max: 1.23 | Avg: ~0.95
- Nulls: 0
- USD always = 1.0
