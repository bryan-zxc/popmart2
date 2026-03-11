-- l20drv_sales_usd: Foundation table - normalize all sales to USD for analysis
-- Primary key: (order_number, line_item)
-- Dependencies: l10wrk_sales, l10wrk_products, l10wrk_exchange_rates

CREATE OR REPLACE TABLE l20drv_sales_usd AS
SELECT
    s.order_number,
    s.line_item,
    s.order_date,
    s.delivery_date,
    s.customer_key,
    s.store_key,
    s.product_key,
    s.quantity,
    s.currency_code,
    p.unit_price_usd,
    p.unit_cost_usd,
    p.brand,
    p.category,
    p.subcategory,
    e.exchange_rate,
    -- Calculate USD values
    (p.unit_price_usd * s.quantity) / e.exchange_rate AS revenue_usd,
    (p.unit_cost_usd * s.quantity) AS cost_usd,
    ((p.unit_price_usd * s.quantity) / e.exchange_rate) - (p.unit_cost_usd * s.quantity) AS margin_usd
FROM l10wrk_sales s
INNER JOIN l10wrk_products p ON s.product_key = p.product_key
LEFT JOIN l10wrk_exchange_rates e
    ON s.order_date = e.date
    AND s.currency_code = e.currency
WHERE s.order_date >= '2020-01-01'
  AND s.order_date < '2022-01-01';
