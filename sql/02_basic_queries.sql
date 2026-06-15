-- Listar todas as vendas
SELECT *
FROM sales;

-- Faturamento total
SELECT
    ROUND(SUM(quantity * unit_price), 2) AS total_revenue
FROM sales;

-- Faturamento por categoria
SELECT
    category,
    ROUND(SUM(quantity * unit_price), 2) AS revenue
FROM sales
GROUP BY category
ORDER BY revenue DESC;

-- Quantidade vendida por produto
SELECT
    product,
    SUM(quantity) AS total_quantity
FROM sales
GROUP BY product
ORDER BY total_quantity DESC;
