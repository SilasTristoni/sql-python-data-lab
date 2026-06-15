from src.analysis import (
    calculate_average_ticket,
    calculate_total_revenue,
    count_orders,
    get_best_selling_product,
    get_customer_ranking,
    get_revenue_by_category,
)
from src.database import (
    create_table,
    fetch_sales,
    get_connection,
    insert_sales,
    read_sales_from_csv,
)


def main() -> None:
    """Run the initial data lab pipeline."""
    csv_sales = read_sales_from_csv()

    with get_connection() as connection:
        create_table(connection)
        insert_sales(connection, csv_sales)
        sales = fetch_sales(connection)

    total_revenue = calculate_total_revenue(sales)
    total_orders = count_orders(sales)
    average_ticket = calculate_average_ticket(sales)
    best_product = get_best_selling_product(sales)
    revenue_by_category = get_revenue_by_category(sales)
    customer_ranking = get_customer_ranking(sales)

    print("=== SQL Python Data Lab ===")
    print(f"Total de pedidos: {total_orders}")
    print(f"Faturamento total: R$ {total_revenue:.2f}")
    print(f"Ticket médio: R$ {average_ticket:.2f}")
    print(f"Produto mais vendido: {best_product}")
    print("\nFaturamento por categoria:")

    for category, revenue in sorted(revenue_by_category.items()):
        print(f"- {category}: R$ {revenue:.2f}")

    print("\nTop 3 clientes por faturamento:")

    for item in customer_ranking[:3]:
        print(
            f"- {item['customer']}: "
            f"{item['total_orders']} pedido(s), "
            f"R$ {item['total_revenue']:.2f}, "
            f"ticket medio R$ {item['average_ticket']:.2f}"
        )


if __name__ == "__main__":
    main()
