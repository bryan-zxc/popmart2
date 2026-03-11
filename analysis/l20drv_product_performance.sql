-- l20drv_product_performance: Aggregate sales by product for profitability analysis
-- Primary key: product_key
-- Dependencies: l10wrk_products, l20drv_sales_usd

CREATE OR REPLACE TABLE l20drv_product_performance AS
SELECT
    p.product_key,
    p.product_name,
    p.brand,
    p.category,
    p.subcategory,
    COUNT(DISTINCT s.order_number) AS order_count,
    SUM(s.quantity) AS units_sold,
    SUM(s.revenue_usd) AS revenue_usd,
    SUM(s.cost_usd) AS cost_usd,
    SUM(s.margin_usd) AS margin_usd,
    ROUND(100.0 * SUM(s.margin_usd) / NULLIF(SUM(s.revenue_usd), 0), 2) AS margin_pct
FROM l10wrk_products p
LEFT JOIN l20drv_sales_usd s ON p.product_key = s.product_key
GROUP BY p.product_key, p.product_name, p.brand, p.category, p.subcategory;
