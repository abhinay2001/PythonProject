from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator

from pipeline import run_pipeline


default_args = {"owner": "airflow"}


with DAG(
    dag_id="retail_etl_mysql_to_postgres",
    default_args=default_args,
    start_date=datetime(2026, 1, 1),
    schedule=None,          # run manually for now
    catchup=False,
    tags=["etl", "retail"],
) as dag:

    run_etl = PythonOperator(
        task_id="run_etl",
        python_callable=run_pipeline,
        op_kwargs={"env": "dev"},
    )