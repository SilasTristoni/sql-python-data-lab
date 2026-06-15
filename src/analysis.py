from collections import defaultdict
from typing import Dict, Iterable, List, Set, TypedDict


class Sale(TypedDict):
    order_id: int
    order_date: str
    customer: str
    product: str
    category: str
    quantity: int
    unit_price: float


class CustomerRankingItem(TypedDict):
    customer: str
    total_orders: int
    total_revenue: float
    average_ticket: float


def calculate_total_revenue(sales: Iterable[Sale]) -> float:
    """Calculate total revenue based on quantity and unit price."""
    return round(sum(item["quantity"] * item["unit_price"] for item in sales), 2)


def count_orders(sales: Iterable[Sale]) -> int:
    """Count unique order IDs."""
    return len({item["order_id"] for item in sales})


def calculate_average_ticket(sales: List[Sale]) -> float:
    """Calculate average ticket per unique order."""
    orders = count_orders(sales)

    if orders == 0:
        return 0.0

    return round(calculate_total_revenue(sales) / orders, 2)


def get_revenue_by_category(sales: Iterable[Sale]) -> Dict[str, float]:
    """Group revenue by category."""
    result: Dict[str, float] = defaultdict(float)

    for item in sales:
        result[item["category"]] += item["quantity"] * item["unit_price"]

    return {category: round(total, 2) for category, total in result.items()}


def get_best_selling_product(sales: Iterable[Sale]) -> str:
    """Return the product with the highest quantity sold."""
    quantities: Dict[str, int] = defaultdict(int)

    for item in sales:
        quantities[item["product"]] += item["quantity"]

    if not quantities:
        return "Nenhum produto encontrado"

    return max(quantities, key=quantities.get)


def get_customer_ranking(sales: Iterable[Sale]) -> List[CustomerRankingItem]:
    """Return customers ordered by highest revenue."""
    revenues: Dict[str, float] = defaultdict(float)
    orders: Dict[str, Set[int]] = defaultdict(set)

    for item in sales:
        customer = item["customer"]
        revenues[customer] += item["quantity"] * item["unit_price"]
        orders[customer].add(item["order_id"])

    ranking: List[CustomerRankingItem] = []

    for customer, total in revenues.items():
        total_orders = len(orders[customer])
        total_revenue = round(total, 2)
        average_ticket = round(total_revenue / total_orders, 2) if total_orders else 0.0

        ranking.append(
            {
                "customer": customer,
                "total_orders": total_orders,
                "total_revenue": total_revenue,
                "average_ticket": average_ticket,
            }
        )

    return sorted(ranking, key=lambda item: item["total_revenue"], reverse=True)
