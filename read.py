from util import get_connection
from mysql.connector import Error as MySQLError

def read_table(db_details, table_name, limit=0):
    SOURCE_DB = db_details['SOURCE_DB']
    connection = get_connection(
        db_type=SOURCE_DB['DB_TYPE'],
        db_host=SOURCE_DB['DB_HOST'],
        db_name=SOURCE_DB['DB_NAME'],
        db_user=SOURCE_DB['DB_USER'],
        db_pass=SOURCE_DB['DB_PASS'],
        db_port=SOURCE_DB.get('DB_PORT')
    )
    cursor = connection.cursor()

    query = f"SELECT * FROM {table_name}" if limit == 0 else f"SELECT * FROM {table_name} LIMIT {limit}"

    try:
        cursor.execute(query)
        data = cursor.fetchall()
        column_names = cursor.column_names
        return data, column_names
    except MySQLError as e:
        # 1146 = table doesn't exist
        if getattr(e, "errno", None) == 1146:
            print(f"Skipping {table_name}: table not found in MySQL")
            return [], ()
        raise
    finally:
        connection.close()
