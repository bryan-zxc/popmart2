-- l30exp_store_insights: Top 10 and bottom 10 stores with category mix insights
-- Primary key: store_key
-- Dependencies: l30exp_store_ranking, l20drv_store_product_mix

CREATE OR REPLACE TABLE l30exp_store_insights AS
WITH ranked_stores AS (
    SELECT *,
        ROW_NUMBER() OVER (ORDER BY revenue_usd DESC) AS top_rank,
        ROW_NUMBER() OVER (ORDER BY revenue_usd ASC) AS bottom_rank
    FROM l30exp_store_ranking
    WHERE store_type = 'Physical'  -- Exclude online for top/bottom comparison
),
top_bottom AS (
    SELECT *, 'Top 10' AS performance_group
    FROM ranked_stores
    WHERE top_rank <= 10
    UNION ALL
    SELECT *, 'Bottom 10' AS performance_group
    FROM ranked_stores
    WHERE bottom_rank <= 10
),
category_mix AS (
    SELECT
        store_key,
        category,
        revenue_usd AS category_revenue,
        ROUND(100.0 * revenue_usd / SUM(revenue_usd) OVER (PARTITION BY store_key), 2) AS pct_of_store_revenue
    FROM l20drv_store_product_mix
)
SELECT
    tb.*,
    -- Add dominant category (highest % of revenue)
    (SELECT category FROM category_mix cm
     WHERE cm.store_key = tb.store_key
     ORDER BY pct_of_store_revenue DESC
     LIMIT 1) AS dominant_category
FROM top_bottom tb
ORDER BY performance_group, top_rank, bottom_rank;
