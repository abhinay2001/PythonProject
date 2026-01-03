from env_loader import load_dotenv
load_dotenv()

import config

print("CONFIG FILE USED:", getattr(config, "__file__", "unknown"))
import psycopg2

import pandas as pd
from config import DB_DETAILS
import mysql.connector as mc


def load_db_details(env):
    return DB_DETAILS[env]

def get_mysql_connection(db_host, db_user, db_pass,db_name, db_port=3306):
    print("MYSQL connect using:",
          db_host, db_port, db_user, db_name,
          "pass_len=", len(db_pass),
          "pass_repr=", repr(db_pass))

    try:
        return mc.connect(host=db_host,
                          user=db_user,
                          password=db_pass,
                          database=db_name,
                          port=int(db_port))
    except mc.Error as error:
        raise RuntimeError(f"MySQL connection failed {error}") from error

def get_pg_connection(db_host, db_user, db_pass,db_name, db_port=5432):
    try:
        return psycopg2.connect(host=db_host,
                                user=db_user,
                                password=db_pass,
                                database=db_name,
                                port=int(db_port))
    except psycopg2.Error as error:
        raise RuntimeError(f"Postgres connection failed: {error}") from error

def get_connection(db_type, db_host, db_name, db_user, db_pass, db_port=None):
    if db_type == 'mysql':
        return get_mysql_connection(db_host, db_user, db_pass, db_name, db_port or 3306)
    elif db_type == 'postgres':
        return get_pg_connection(db_host, db_user, db_pass, db_name, db_port or 5432)
    else:
        raise ValueError(f"Unsupported db_type: {db_type}")

def get_tables(path):
    tables = pd.read_csv(path, sep=":")
    return tables.query('to_be_loaded == "yes"')
