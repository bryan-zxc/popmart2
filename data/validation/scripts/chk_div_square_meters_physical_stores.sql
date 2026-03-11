-- Check: physical stores have non-null square_meters (division safety)
-- Expectation: only store_key=0 (online) should have null square_meters
SELECT store_key, country, state, square_meters
FROM l10wrk_stores
WHERE store_key != 0  -- Exclude online store
  AND (square_meters IS NULL OR square_meters = 0)
ORDER BY store_key;
