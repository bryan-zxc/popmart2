-- Check: store_key uniqueness in l10wrk_stores
-- Expectation: store_key should be unique (primary key)
SELECT store_key, COUNT(*) AS duplicate_count
FROM l10wrk_stores
GROUP BY store_key
HAVING COUNT(*) > 1
ORDER BY duplicate_count DESC;
