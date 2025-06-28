
-- Top 5 customers by revenue
SELECT customer_id, SUM(amount) AS total_revenue
FROM sales
GROUP BY customer_id
ORDER BY total_revenue DESC
LIMIT 5;

-- Revenue per month
SELECT DATE_TRUNC('month', order_date) AS month, SUM(amount) AS monthly_revenue
FROM sales
GROUP BY month
ORDER BY month;
