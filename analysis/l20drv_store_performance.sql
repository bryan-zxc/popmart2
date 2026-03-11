-- l20drv_store_performance: Aggregate sales by store for performance ranking
-- Primary key: store_key
-- Dependencies: l10wrk_stores, l20drv_sales_usd

CREATE OR REPLACE TABLE l20drv_store_performance AS
SELECT
    st.store_key,
    st.country,
    st.state,
    st.square_meters,
    st.open_date,
    COUNT(DISTINCT s.order_number) AS order_count,
    SUM(s.quantity) AS units_sold,
    SUM(s.revenue_usd) AS revenue_usd,
    SUM(s.cost_usd) AS cost_usd,
    SUM(s.margin_usd) AS margin_usd,
    ROUND(100.0 * SUM(s.margin_usd) / NULLIF(SUM(s.revenue_usd), 0), 2) AS margin_pct,
    ROUND(SUM(s.revenue_usd) / NULLIF(COUNT(DISTINCT s.order_number), 0), 2) AS avg_order_value,
    -- Efficiency metric (null for online store)
    ROUND(SUM(s.revenue_usd) / NULLIF(st.square_meters, 0), 2) AS revenue_per_sqm
FROM l10wrk_stores st
LEFT JOIN l20drv_sales_usd s ON st.store_key = s.store_key
GROUP BY st.store_key, st.country, st.state, st.square_meters, st.open_date;
