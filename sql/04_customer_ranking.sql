-- Ranking de clientes por faturamento
SELECT
    customer AS customer_name,
    COUNT(DISTINCT order_id) AS total_orders,
    ROUND(SUM(quantity * unit_price), 2) AS total_revenue,
    ROUND(SUM(quantity * unit_price) / COUNT(DISTINCT order_id), 2) AS average_ticket
FROM sales
GROUP BY customer
ORDER BY total_revenue DESC;
