-- Check: no zero or null exchange rates (division safety)
-- Expectation: all exchange rates should be positive numbers
SELECT date, currency, exchange_rate
FROM l10wrk_exchange_rates
WHERE exchange_rate = 0 OR exchange_rate IS NULL
ORDER BY date, currency;
