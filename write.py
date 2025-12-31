from util import get_connection

def build_insert_query(table_name, column_names):
    cols = ", ".join(column_names)
    placeholders = ", ".join(["%s"] * len(column_names))
    return f"INSERT INTO {table_name} ({cols}) VALUES ({placeholders})"


def insert_data(connection, cursor, query, data, batch_size=100):
    for i in range(0, len(data), batch_size):
        batch = data[i:i+batch_size]
        cursor.executemany(query, batch)
        connection.commit()


def load_table(db_details, data, column_names, table_name):
    TARGET_DB = db_details['TARGET_DB']

    connection = get_connection(db_type=TARGET_DB['DB_TYPE'],
                                db_host=TARGET_DB['DB_HOST'],
                                db_name=TARGET_DB['DB_NAME'],
                                db_user=TARGET_DB['DB_USER'],
                                db_pass=TARGET_DB['DB_PASS'],
                                db_port=TARGET_DB.get('DB_PORT')
                                )
    cursor = connection.cursor()
    query = build_insert_query(table_name, column_names)
    print(query)
    insert_data(connection, cursor, query, data, batch_size=100)

    connection.close()