-- l30exp_store_ranking: Complete store performance ranking
-- Primary key: store_key
-- Dependencies: l20drv_store_performance

CREATE OR REPLACE TABLE l30exp_store_ranking AS
SELECT
    store_key,
    country,
    state,
    square_meters,
    open_date,
    order_count,
    units_sold,
    revenue_usd,
    cost_usd,
    margin_usd,
    margin_pct,
    avg_order_value,
    revenue_per_sqm,
    -- Rankings
    RANK() OVER (ORDER BY revenue_usd DESC) AS revenue_rank,
    RANK() OVER (ORDER BY margin_usd DESC) AS margin_rank,
    RANK() OVER (ORDER BY revenue_per_sqm DESC NULLS LAST) AS efficiency_rank,
    -- Classification
    CASE WHEN store_key = 0 THEN 'Online'
         ELSE 'Physical' END AS store_type,
    -- Years in operation during analysis period
    CASE WHEN open_date >= '2020-01-01' THEN
        ROUND((DATE '2021-12-31' - open_date) / 365.25, 1)
    ELSE
        2.0
    END AS years_active_in_period
FROM l20drv_store_performance
ORDER BY revenue_usd DESC;
