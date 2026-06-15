from src.reports import export_summary_report


def test_export_summary_report(tmp_path):
    report_path = tmp_path / "summary.csv"

    result = export_summary_report(
        total_orders=3,
        total_revenue=100.0,
        average_ticket=33.33,
        best_selling_product="Produto X",
        report_path=report_path,
    )

    assert result == report_path
    assert report_path.read_text(encoding="utf-8") == (
        "total_orders,total_revenue,average_ticket,best_selling_product\n"
        "3,100.00,33.33,Produto X\n"
    )
