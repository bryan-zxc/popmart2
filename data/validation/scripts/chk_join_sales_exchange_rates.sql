-- Check: all 2020-2021 sales have matching exchange rates
-- Expectation: 100% match rate for currency conversion
SELECT
    s.order_date,
    s.currency_code,
    COUNT(*) AS sales_rows_without_rate,
    SUM(s.quantity) AS total_quantity_affected
FROM l10wrk_sales s
LEFT JOIN l10wrk_exchange_rates e
    ON s.order_date = e.date
    AND s.currency_code = e.currency
WHERE s.order_date >= '2020-01-01'
  AND s.order_date < '2022-01-01'
  AND e.exchange_rate IS NULL
GROUP BY s.order_date, s.currency_code
ORDER BY s.order_date, s.currency_code;
