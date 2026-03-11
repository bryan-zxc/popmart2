-- Check: negative quantities in sales
-- Expectation: quantities should be positive (negative may indicate returns)
SELECT order_number, line_item, order_date, product_key, quantity
FROM l10wrk_sales
WHERE quantity < 0
ORDER BY order_date;
