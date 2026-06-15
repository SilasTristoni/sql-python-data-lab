import csv
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[1]
REPORTS_DIR = ROOT_DIR / "reports"
SUMMARY_REPORT_PATH = REPORTS_DIR / "summary.csv"


def export_summary_report(
    total_orders: int,
    total_revenue: float,
    average_ticket: float,
    best_selling_product: str,
    report_path: Path = SUMMARY_REPORT_PATH,
) -> Path:
    """Export the main project indicators to a CSV file."""
    report_path.parent.mkdir(exist_ok=True)

    with report_path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "total_orders",
                "total_revenue",
                "average_ticket",
                "best_selling_product",
            ],
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerow(
            {
                "total_orders": total_orders,
                "total_revenue": f"{total_revenue:.2f}",
                "average_ticket": f"{average_ticket:.2f}",
                "best_selling_product": best_selling_product,
            }
        )

    return report_path
