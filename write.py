from logger import get_logger
from util import get_connection
from datetime import datetime

log = get_logger(__name__)

PK_MAP = {
    "departments": "department_id",
    "customers": "customer_id",
    "categories": "category_id",
    "products": "product_id",
    "orders": "order_id",
    "order_items": "order_item_id",
}


def build_insert_query(table_name, column_names):
    cols = ", ".join(column_names)
    placeholders = ", ".join(["%s"] * len(column_names))

    pk_col = PK_MAP.get(table_name)
    if not pk_col:
        raise ValueError(f"No primary key mapping defined for table: {table_name}")

    return f"""
        INSERT INTO {table_name} ({cols})
        VALUES ({placeholders})
        ON CONFLICT ({pk_col})
        DO NOTHING
    """


def insert_data(connection, cursor, query, data, batch_size=100):
    total_inserted = 0
    batch = []

    for rec in data:
        batch.append(rec)
        if len(batch) >= batch_size:
            cursor.executemany(query, batch)
            total_inserted += cursor.rowcount
            connection.commit()
            batch = []

    if batch:
        cursor.executemany(query, batch)
        total_inserted += cursor.rowcount
        connection.commit()

    return total_inserted


def load_table(db_details, data, column_names, table_name):
    TARGET_DB = db_details["TARGET_DB"]

    connection = get_connection(
        db_type=TARGET_DB["DB_TYPE"],
        db_host=TARGET_DB["DB_HOST"],
        db_name=TARGET_DB["DB_NAME"],
        db_user=TARGET_DB["DB_USER"],
        db_pass=TARGET_DB["DB_PASS"],
        db_port=TARGET_DB.get("DB_PORT"),
    )

    cursor = connection.cursor()
    try:
        query = build_insert_query(table_name, column_names)

        if not data:
            log.info("No rows to load for %s (skipping)", table_name)
            return 0

        attempted = len(data)
        inserted = insert_data(connection, cursor, query, data, batch_size=100)
        skipped = attempted - inserted

        log.info(
            "Load complete for %s | attempted=%s inserted=%s skipped=%s",
            table_name, attempted, inserted, skipped
        )

        cursor.execute(
            """
            INSERT INTO ingestion_metadata (table_name, run_at, rows_inserted, rows_attempted, rows_skipped)
            VALUES (%s, %s, %s, %s, %s)
            """,
            (table_name, datetime.utcnow(), inserted, attempted, skipped),
        )
        connection.commit()

        return inserted
    finally:
        cursor.close()
        connection.close()