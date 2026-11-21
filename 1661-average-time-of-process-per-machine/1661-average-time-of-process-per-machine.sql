# Write your MySQL query statement below
select a.machine_id , round(avg( b.timestamp - a.timestamp), 3) as processing_time from Activity a join Activity b on a.machine_id=b.machine_id and a. process_id =b. process_id  where a.activity_type='start' and b.activity_type='end' group by a.machine_id

-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna