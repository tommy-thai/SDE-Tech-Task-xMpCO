select * From js_posts;

-- Write SQL queries to answer these questions using the data you have loaded into BigQuery:
-- 1. Find the top 5 users with the highest number of posts.
SELECT user_id, COUNT(*) AS num_posts
FROM js_posts
GROUP BY user_id
ORDER BY num_posts DESC
LIMIT 5;

-- 2. For each of these top 5 users, calculate the average post length.
WITH TopUsers AS (
    SELECT user_id, COUNT(*) AS num_posts
    FROM js_posts
    GROUP BY user_id
    ORDER BY num_posts DESC
    LIMIT 5
)
SELECT
    tu.user_id,
    AVG(LENGTH(p.body)) AS avg_post_length
FROM
    TopUsers tu
JOIN
    js_posts p ON tu.user_id = p.user_id
GROUP BY
    tu.user_id;



-- 3. Identify the day of the week when the most `lengthy` posts are created (assume all posts were created in the UTC timezone).

WITH LengthyPosts AS (
    SELECT
        CASE STRFTIME('%w', id)
            WHEN '0' THEN 'Sunday'
            WHEN '1' THEN 'Monday'
            WHEN '2' THEN 'Tuesday'
            WHEN '3' THEN 'Wednesday'
            WHEN '4' THEN 'Thursday'
            WHEN '5' THEN 'Friday'
            ELSE 'Saturday'
        END AS day_of_week,
        COUNT(*) AS num_lengthy_posts
    FROM
        js_posts
    WHERE
        status = 'lengthy'
    GROUP BY
        day_of_week
    ORDER BY
        num_lengthy_posts DESC
    LIMIT 1
)
SELECT
    day_of_week
FROM
    LengthyPosts;



