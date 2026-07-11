from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys

# Add the scripts folder to the path (so that extract/transform/load can be imported)
sys.path.append('/opt/airflow/scripts')

from load import load_weather_data

# Default settings for the DAG
default_args = {
    'owner': 'maryam',
    'retries': 1,
    'retry_delay': timedelta(minutes=2),
}

# Define the DAG
with DAG(
    dag_id='weather_etl_pipeline',
    default_args=default_args,
    description='Sialkot weather data ETL pipeline',
    start_date=datetime(2026, 7, 1),
    schedule_interval='@hourly',  # Runs every hour
    catchup=False,  # Skip missed runs from the past
    tags=['weather', 'etl'],
) as dag:

    run_etl = PythonOperator(
        task_id='extract_transform_load',
        python_callable=load_weather_data,
    )

    run_etl
