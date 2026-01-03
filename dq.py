from logger import get_logger
from util import get_connection

log = get_logger(__name__)

def get_row_count(connection, table_name):
    cur = connection.cursor()
    try:
        cur.execute(f"SELECT COUNT(*) FROM {table_name}")
        return cur.fetchone()[0]
    finally:
        cur.close()

def validate_counts(db_details, table_name):
    src = db_details["SOURCE_DB"]
    tgt = db_details["TARGET_DB"]

    src_conn = get_connection(
        db_type=src["DB_TYPE"],
        db_host=src["DB_HOST"],
        db_name=src["DB_NAME"],
        db_user=src["DB_USER"],
        db_pass=src["DB_PASS"],
        db_port=src.get("DB_PORT"),
    )

    tgt_conn = get_connection(
        db_type=tgt["DB_TYPE"],
        db_host=tgt["DB_HOST"],
        db_name=tgt["DB_NAME"],
        db_user=tgt["DB_USER"],
        db_pass=tgt["DB_PASS"],
        db_port=tgt.get("DB_PORT"),
    )

    try:
        src_count = get_row_count(src_conn, table_name)
        tgt_count = get_row_count(tgt_conn, table_name)

        if tgt_count > src_count:
            raise RuntimeError(
                f"DQ failed for {table_name}: target_count({tgt_count}) > source_count({src_count})"
            )

        log.info("DQ OK for %s | source=%s target=%s", table_name, src_count, tgt_count)
        return src_count, tgt_count
    finally:
        src_conn.close()
        tgt_conn.close()