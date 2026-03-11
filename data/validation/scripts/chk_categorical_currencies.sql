-- Check: all currencies in sales exist in exchange_rates table
-- Expectation: categorical consistency - all 5 currencies present
SELECT DISTINCT s.currency_code
FROM l10wrk_sales s
LEFT JOIN (SELECT DISTINCT currency FROM l10wrk_exchange_rates) e
    ON s.currency_code = e.currency
WHERE e.currency IS NULL;
