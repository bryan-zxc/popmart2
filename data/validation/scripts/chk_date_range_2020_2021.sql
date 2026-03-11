-- Check: sales data exists for full 2020-2021 period
-- Expectation: ~24 months covered, earliest ≈ 2020-01-01, latest ≈ 2021-12-31
SELECT
    MIN(order_date) AS earliest_2020_2021,
    MAX(order_date) AS latest_2020_2021,
    COUNT(*) AS total_rows,
    COUNT(DISTINCT DATE_TRUNC('month', order_date)) AS months_covered
FROM l10wrk_sales
WHERE order_date >= '2020-01-01'
  AND order_date < '2022-01-01';
