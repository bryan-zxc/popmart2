-- l20drv_store_product_mix: Category breakdown by store for understanding product mix
-- Primary key: (store_key, category)
-- Dependencies: l20drv_sales_usd, l10wrk_stores

CREATE OR REPLACE TABLE l20drv_store_product_mix AS
SELECT
    s.store_key,
    st.country,
    st.state,
    s.category,
    SUM(s.revenue_usd) AS revenue_usd,
    SUM(s.margin_usd) AS margin_usd,
    SUM(s.quantity) AS units_sold,
    COUNT(DISTINCT s.order_number) AS order_count
FROM l20drv_sales_usd s
INNER JOIN l10wrk_stores st ON s.store_key = st.store_key
GROUP BY s.store_key, st.country, st.state, s.category;
