-- Check: all sales reference valid customers (referential integrity)
-- Expectation: 100% match rate between sales and customers on customer_key
SELECT
    s.customer_key,
    COUNT(*) AS orphaned_sales_rows,
    SUM(s.quantity) AS total_quantity_affected
FROM l10wrk_sales s
LEFT JOIN l10wrk_customers c ON s.customer_key = c.customer_key
WHERE c.customer_key IS NULL
GROUP BY s.customer_key
ORDER BY orphaned_sales_rows DESC;
