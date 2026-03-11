-- Check: product_key uniqueness in l10wrk_products
-- Expectation: product_key should be unique (primary key)
SELECT product_key, COUNT(*) AS duplicate_count
FROM l10wrk_products
GROUP BY product_key
HAVING COUNT(*) > 1
ORDER BY duplicate_count DESC;
