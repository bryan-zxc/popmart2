-- Check: dates beyond expected range (data errors)
-- Expectation: dataset ends Feb 2021, no future dates
SELECT order_number, line_item, order_date, delivery_date
FROM l10wrk_sales
WHERE order_date > '2021-12-31'
   OR delivery_date > '2022-03-31'  -- Allow 90 days for 2021 deliveries
ORDER BY order_date, delivery_date;
