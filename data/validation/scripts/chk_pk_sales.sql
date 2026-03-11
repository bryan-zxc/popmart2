-- Check: (order_number, line_item) composite key uniqueness in l10wrk_sales
-- Expectation: combination should be unique (composite primary key)
SELECT order_number, line_item, COUNT(*) AS duplicate_count
FROM l10wrk_sales
GROUP BY order_number, line_item
HAVING COUNT(*) > 1
ORDER BY duplicate_count DESC;
