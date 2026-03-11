-- Check: all sales reference valid products (referential integrity)
-- Expectation: 100% match rate between sales and products on product_key
SELECT
    s.product_key,
    COUNT(*) AS orphaned_sales_rows,
    SUM(s.quantity) AS total_quantity_affected,
    MIN(s.order_date) AS earliest_order,
    MAX(s.order_date) AS latest_order
FROM l10wrk_sales s
LEFT JOIN l10wrk_products p ON s.product_key = p.product_key
WHERE p.product_key IS NULL
GROUP BY s.product_key
ORDER BY orphaned_sales_rows DESC;
