-- l30exp_product_profitability: Final product analysis for client delivery
-- Primary key: product_key
-- Dependencies: l20drv_product_performance

CREATE OR REPLACE TABLE l30exp_product_profitability AS
SELECT
    product_key,
    product_name,
    brand,
    category,
    subcategory,
    order_count,
    units_sold,
    revenue_usd,
    cost_usd,
    margin_usd,
    margin_pct,
    -- Ranking metrics
    RANK() OVER (ORDER BY margin_usd DESC) AS margin_rank,
    RANK() OVER (ORDER BY revenue_usd DESC) AS revenue_rank,
    -- Flags for quick filtering
    CASE
        WHEN margin_usd < 0 THEN 'Unprofitable'
        WHEN units_sold = 0 THEN 'No Sales'
        ELSE 'Profitable'
    END AS profitability_status
FROM l20drv_product_performance
ORDER BY margin_usd DESC;
