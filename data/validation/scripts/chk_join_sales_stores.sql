-- Check: all sales reference valid stores (referential integrity)
-- Expectation: 100% match rate between sales and stores on store_key
SELECT
    s.store_key,
    COUNT(*) AS orphaned_sales_rows,
    SUM(s.quantity) AS total_quantity_affected,
    MIN(s.order_date) AS earliest_order,
    MAX(s.order_date) AS latest_order
FROM l10wrk_sales s
LEFT JOIN l10wrk_stores st ON s.store_key = st.store_key
WHERE st.store_key IS NULL
GROUP BY s.store_key
ORDER BY orphaned_sales_rows DESC;
