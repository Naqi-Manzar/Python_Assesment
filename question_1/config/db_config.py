import os

DB_CONNECTION = {
    "url": os.getenv("DB_URL", "jdbc:mysql://localhost:3306/sales"),
    "table": "sales_data",
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", "password"),
}
