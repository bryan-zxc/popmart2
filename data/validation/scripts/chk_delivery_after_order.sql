-- Check: delivery_date >= order_date when not null
-- Expectation: deliveries cannot occur before orders (0 rows)
SELECT order_number, line_item, order_date, delivery_date,
       (delivery_date - order_date) AS days_difference
FROM l10wrk_sales
WHERE delivery_date IS NOT NULL
  AND delivery_date < order_date
ORDER BY days_difference;
