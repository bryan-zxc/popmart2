-- Check: customer_key uniqueness in l10wrk_customers
-- Expectation: customer_key should be unique (primary key)
SELECT customer_key, COUNT(*) AS duplicate_count
FROM l10wrk_customers
GROUP BY customer_key
HAVING COUNT(*) > 1
ORDER BY duplicate_count DESC;
