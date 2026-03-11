-- Check: (date, currency) composite key uniqueness in l10wrk_exchange_rates
-- Expectation: combination should be unique (composite primary key)
SELECT date, currency, COUNT(*) AS duplicate_count
FROM l10wrk_exchange_rates
GROUP BY date, currency
HAVING COUNT(*) > 1
ORDER BY duplicate_count DESC;
