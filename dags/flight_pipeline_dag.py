from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from scripts.extract import extract_flight_data
from scripts.transform import transform_flight_data
from scripts.load import load_flight_data

default_args = {
    "owner": "Pranjal",
    "retries": 2,
    "retry_delay": timedelta(minutes=2),
}

with DAG(
    dag_id="flight_operations_pipeline",
    description="Flight Operations ETL Pipeline",
    start_date=datetime(2026, 1, 1),
    schedule="@daily",
    catchup=False,
    default_args=default_args,
    tags=["etl", "flight", "portfolio"],
) as dag:

    extract_task = PythonOperator(
        task_id="extract_flight_data",
        python_callable=extract_flight_data,
    )

    transform_task = PythonOperator(
        task_id="transform_flight_data",
        python_callable=transform_flight_data,
    )

    load_task = PythonOperator(
        task_id="load_flight_data",
        python_callable=load_flight_data,
    )

    extract_task >> transform_task >> load_task