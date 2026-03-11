# Data Check Register

| Check | Description | Outcome | Script | In DV Report | Last Ran |
|-------|-------------|---------|--------|--------------|----------|
| chk_pk_customers | Verify customer_key uniqueness in l10wrk_customers | PASS — all 15,266 customer_key values are unique (0 duplicates) | [chk_pk_customers.sql](scripts/chk_pk_customers.sql) | no | 2026-03-11 |
| chk_pk_products | Verify product_key uniqueness in l10wrk_products | PASS — all 2,517 product_key values are unique (0 duplicates) | [chk_pk_products.sql](scripts/chk_pk_products.sql) | no | 2026-03-11 |
| chk_pk_stores | Verify store_key uniqueness in l10wrk_stores | PASS — all 67 store_key values are unique (0 duplicates) | [chk_pk_stores.sql](scripts/chk_pk_stores.sql) | no | 2026-03-11 |
| chk_pk_sales | Verify (order_number, line_item) composite key uniqueness in l10wrk_sales | PASS — all 62,884 composite keys are unique (0 duplicates) | [chk_pk_sales.sql](scripts/chk_pk_sales.sql) | no | 2026-03-11 |
| chk_pk_exchange_rates | Verify (date, currency) composite key uniqueness in l10wrk_exchange_rates | PASS — all 11,215 composite keys are unique (0 duplicates) | [chk_pk_exchange_rates.sql](scripts/chk_pk_exchange_rates.sql) | no | 2026-03-11 |
| chk_join_sales_products | Verify all sales reference valid products | PASS — 100% match rate, all 62,884 sales rows have valid product_key | [chk_join_sales_products.sql](scripts/chk_join_sales_products.sql) | no | 2026-03-11 |
| chk_join_sales_stores | Verify all sales reference valid stores | PASS — 100% match rate, all 62,884 sales rows have valid store_key | [chk_join_sales_stores.sql](scripts/chk_join_sales_stores.sql) | no | 2026-03-11 |
| chk_join_sales_customers | Verify all sales reference valid customers | PASS — 100% match rate, all 62,884 sales rows have valid customer_key | [chk_join_sales_customers.sql](scripts/chk_join_sales_customers.sql) | no | 2026-03-11 |
| chk_join_sales_exchange_rates | Verify all 2020-2021 sales have matching exchange rates | PASS — 100% match rate, all 12,238 sales (2020-2021) have exchange rates | [chk_join_sales_exchange_rates.sql](scripts/chk_join_sales_exchange_rates.sql) | no | 2026-03-11 |
| chk_categorical_currencies | Verify all currencies in sales exist in exchange_rates | PASS — all 5 currencies (USD, EUR, GBP, CAD, AUD) present in both tables | [chk_categorical_currencies.sql](scripts/chk_categorical_currencies.sql) | no | 2026-03-11 |
| chk_div_exchange_rate_zero | Check for zero or null exchange rates | PASS — no zero or null exchange rates found (0 rows) | [chk_div_exchange_rate_zero.sql](scripts/chk_div_exchange_rate_zero.sql) | no | 2026-03-11 |
| chk_div_square_meters_physical_stores | Verify physical stores have non-null square_meters | PASS — only online store (store_key=0) has null square_meters (0 physical stores affected) | [chk_div_square_meters_physical_stores.sql](scripts/chk_div_square_meters_physical_stores.sql) | no | 2026-03-11 |
| chk_negatives_quantity | Check for negative quantities | PASS — no negative quantities found (0 rows) | [chk_negatives_quantity.sql](scripts/chk_negatives_quantity.sql) | no | 2026-03-11 |
| chk_negatives_prices_costs | Check for negative unit prices or costs | PASS — no negative prices or costs found (0 rows) | [chk_negatives_prices_costs.sql](scripts/chk_negatives_prices_costs.sql) | no | 2026-03-11 |
| chk_date_range_2020_2021 | Verify sales exist across full 2020-2021 period | PASS — 12,238 rows spanning 2020-01-01 to 2021-02-20 (14 months covered) | [chk_date_range_2020_2021.sql](scripts/chk_date_range_2020_2021.sql) | no | 2026-03-11 |
| chk_delivery_after_order | Verify delivery_date >= order_date when not null | PASS — all delivery dates occur on or after order dates (0 violations) | [chk_delivery_after_order.sql](scripts/chk_delivery_after_order.sql) | no | 2026-03-11 |
| chk_future_dates | Check for dates beyond expected range | PASS — no dates beyond 2021-12-31 found (0 rows) | [chk_future_dates.sql](scripts/chk_future_dates.sql) | no | 2026-03-11 |
