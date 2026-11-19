# Write your MySQL query statement below
-- This query returns the IDs of days where the temperature increased compared to the previous day.
-- It self‑joins the Weather table on consecutive dates (datediff = 1) and filters where the temperature rose.
-- Time Complexity: O(N) where N is the number of records, due to a single self‑join.
-- Space Complexity: O(N) for the join operation's intermediate result.
select w1.id
from Weather w1
join Weather w2
  on datediff(w1.recordDate, w2.recordDate) = 1
where w1.temperature > w2.temperature;

-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna