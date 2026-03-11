-- Check: negative unit prices or costs in products
-- Expectation: prices and costs should be positive
SELECT product_key, product_name, unit_price_usd, unit_cost_usd
FROM l10wrk_products
WHERE unit_price_usd < 0 OR unit_cost_usd < 0
ORDER BY product_key;
