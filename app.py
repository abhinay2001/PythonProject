import sys

from logger import get_logger
from util import get_tables, load_db_details
from read import read_table
from write import load_table

log = get_logger(__name__)


def main():
    """program takes at least one argument"""
    env = sys.argv[1]
    db_details = load_db_details(env)

    source_db = db_details["SOURCE_DB"]
    log.info(
        "SOURCE_DB: type=%s host=%s port=%s user=%s name=%s",
        source_db.get("DB_TYPE"),
        source_db.get("DB_HOST"),
        source_db.get("DB_PORT"),
        source_db.get("DB_USER"),
        source_db.get("DB_NAME"),
    )

    tables = get_tables("table_list")
    for table_name in tables["table_name"]:
        log.info("Reading data for %s", table_name)
        data, column_names = read_table(db_details, table_name)

        log.info("Columns for %s: %s", table_name, column_names)
        log.info("Loading data for %s", table_name)
        load_table(db_details, data, column_names, table_name)


if __name__ == "__main__":
    main()