from src.analysis import (
    calculate_average_ticket,
    calculate_total_revenue,
    count_orders,
    get_best_selling_product,
    get_customer_ranking,
    get_revenue_by_category,
)


SAMPLE_SALES = [
    {
        "order_id": 1,
        "order_date": "2026-01-01",
        "customer": "Cliente A",
        "product": "Produto X",
        "category": "Categoria 1",
        "quantity": 2,
        "unit_price": 10.0,
    },
    {
        "order_id": 2,
        "order_date": "2026-01-02",
        "customer": "Cliente B",
        "product": "Produto Y",
        "category": "Categoria 2",
        "quantity": 1,
        "unit_price": 50.0,
    },
    {
        "order_id": 3,
        "order_date": "2026-01-03",
        "customer": "Cliente C",
        "product": "Produto X",
        "category": "Categoria 1",
        "quantity": 3,
        "unit_price": 10.0,
    },
]

CUSTOMER_RANKING_SALES = [
    {
        "order_id": 1,
        "order_date": "2026-01-01",
        "customer": "Cliente A",
        "product": "Produto X",
        "category": "Categoria 1",
        "quantity": 2,
        "unit_price": 10.0,
    },
    {
        "order_id": 2,
        "order_date": "2026-01-02",
        "customer": "Cliente B",
        "product": "Produto Y",
        "category": "Categoria 2",
        "quantity": 1,
        "unit_price": 50.0,
    },
    {
        "order_id": 3,
        "order_date": "2026-01-03",
        "customer": "Cliente A",
        "product": "Produto Z",
        "category": "Categoria 1",
        "quantity": 3,
        "unit_price": 20.0,
    },
]


def test_calculate_total_revenue():
    assert calculate_total_revenue(SAMPLE_SALES) == 100.0


def test_count_orders():
    assert count_orders(SAMPLE_SALES) == 3


def test_calculate_average_ticket():
    assert calculate_average_ticket(SAMPLE_SALES) == 33.33


def test_get_best_selling_product():
    assert get_best_selling_product(SAMPLE_SALES) == "Produto X"


def test_get_revenue_by_category():
    assert get_revenue_by_category(SAMPLE_SALES) == {
        "Categoria 1": 50.0,
        "Categoria 2": 50.0,
    }


def test_get_customer_ranking_orders_by_highest_revenue():
    ranking = get_customer_ranking(CUSTOMER_RANKING_SALES)

    assert [item["customer"] for item in ranking] == ["Cliente A", "Cliente B"]


def test_get_customer_ranking_calculates_total_orders():
    ranking = get_customer_ranking(CUSTOMER_RANKING_SALES)

    assert ranking[0]["total_orders"] == 2
    assert ranking[1]["total_orders"] == 1


def test_get_customer_ranking_calculates_total_revenue():
    ranking = get_customer_ranking(CUSTOMER_RANKING_SALES)

    assert ranking[0]["total_revenue"] == 80.0
    assert ranking[1]["total_revenue"] == 50.0


def test_get_customer_ranking_calculates_average_ticket():
    ranking = get_customer_ranking(CUSTOMER_RANKING_SALES)

    assert ranking[0]["average_ticket"] == 40.0
    assert ranking[1]["average_ticket"] == 50.0
