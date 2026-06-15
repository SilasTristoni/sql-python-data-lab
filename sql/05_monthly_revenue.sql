-- Analise mensal de faturamento
SELECT
    SUBSTR(order_date, 1, 7) AS month,
    COUNT(DISTINCT order_id) AS total_orders,
    SUM(quantity) AS total_items_sold,
    ROUND(SUM(quantity * unit_price), 2) AS total_revenue
FROM sales
GROUP BY SUBSTR(order_date, 1, 7)
ORDER BY month;
