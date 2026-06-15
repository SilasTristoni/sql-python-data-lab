-- Ticket médio por pedido
SELECT
    ROUND(SUM(quantity * unit_price) / COUNT(DISTINCT order_id), 2) AS average_ticket
FROM sales;

-- Ranking de clientes por faturamento
SELECT
    customer,
    ROUND(SUM(quantity * unit_price), 2) AS revenue
FROM sales
GROUP BY customer
ORDER BY revenue DESC;

-- Faturamento mensal
SELECT
    SUBSTR(order_date, 1, 7) AS month,
    ROUND(SUM(quantity * unit_price), 2) AS revenue
FROM sales
GROUP BY SUBSTR(order_date, 1, 7)
ORDER BY month;
