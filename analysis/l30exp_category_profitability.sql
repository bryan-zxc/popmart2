-- l30exp_category_profitability: Category and subcategory rollups for executive view
-- Primary key: (category, subcategory)
-- Dependencies: l20drv_product_performance

CREATE OR REPLACE TABLE l30exp_category_profitability AS
SELECT
    category,
    subcategory,
    COUNT(DISTINCT product_key) AS product_count,
    SUM(order_count) AS total_orders,
    SUM(units_sold) AS total_units,
    SUM(revenue_usd) AS revenue_usd,
    SUM(cost_usd) AS cost_usd,
    SUM(margin_usd) AS margin_usd,
    ROUND(100.0 * SUM(margin_usd) / NULLIF(SUM(revenue_usd), 0), 2) AS margin_pct,
    RANK() OVER (ORDER BY SUM(margin_usd) DESC) AS category_rank
FROM l20drv_product_performance
GROUP BY category, subcategory
ORDER BY SUM(margin_usd) DESC;
