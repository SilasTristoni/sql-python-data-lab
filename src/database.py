import csv
import sqlite3
from pathlib import Path
from typing import List

from src.analysis import Sale


ROOT_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT_DIR / "data"
CSV_PATH = DATA_DIR / "sample_sales.csv"
DATABASE_PATH = DATA_DIR / "lab.db"


def get_connection() -> sqlite3.Connection:
    """Create a SQLite connection."""
    DATA_DIR.mkdir(exist_ok=True)
    return sqlite3.connect(DATABASE_PATH)


def create_table(connection: sqlite3.Connection) -> None:
    """Create the sales table."""
    connection.execute(
        """
        DROP TABLE IF EXISTS sales;
        """
    )

    connection.execute(
        """
        CREATE TABLE sales (
            order_id INTEGER PRIMARY KEY,
            order_date TEXT NOT NULL,
            customer TEXT NOT NULL,
            product TEXT NOT NULL,
            category TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            unit_price REAL NOT NULL
        );
        """
    )

    connection.commit()


def read_sales_from_csv(csv_path: Path = CSV_PATH) -> List[Sale]:
    """Read sales from the CSV file."""
    sales: List[Sale] = []

    with csv_path.open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            sales.append(
                {
                    "order_id": int(row["order_id"]),
                    "order_date": row["order_date"],
                    "customer": row["customer"],
                    "product": row["product"],
                    "category": row["category"],
                    "quantity": int(row["quantity"]),
                    "unit_price": float(row["unit_price"]),
                }
            )

    return sales


def insert_sales(connection: sqlite3.Connection, sales: List[Sale]) -> None:
    """Insert sales data into SQLite."""
    connection.executemany(
        """
        INSERT INTO sales (
            order_id,
            order_date,
            customer,
            product,
            category,
            quantity,
            unit_price
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        [
            (
                sale["order_id"],
                sale["order_date"],
                sale["customer"],
                sale["product"],
                sale["category"],
                sale["quantity"],
                sale["unit_price"],
            )
            for sale in sales
        ],
    )

    connection.commit()


def fetch_sales(connection: sqlite3.Connection) -> List[Sale]:
    """Fetch all sales from SQLite."""
    cursor = connection.execute(
        """
        SELECT
            order_id,
            order_date,
            customer,
            product,
            category,
            quantity,
            unit_price
        FROM sales
        ORDER BY order_id
        """
    )

    return [
        {
            "order_id": int(row[0]),
            "order_date": str(row[1]),
            "customer": str(row[2]),
            "product": str(row[3]),
            "category": str(row[4]),
            "quantity": int(row[5]),
            "unit_price": float(row[6]),
        }
        for row in cursor.fetchall()
    ]
