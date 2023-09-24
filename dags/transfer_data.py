from airflow import DAG
from datetime import datetime
from airflow.operators.generic_transfer import GenericTransfer

with DAG(dag_id='extract_data',
         start_date=datetime(2023, 9, 1), schedule_interval='@daily',
         catchup=False) as dag:
    
        transfer_data = GenericTransfer(
            task_id='transfer_database',
            sql='''SELECT state,account_length,area_code,phone_number,international_plan,voice_mail_plan,number_vmail_messages,total_day_minutes,total_day_calls,total_day_charge,total_eve_minutes,total_eve_calls,total_eve_charge,total_night_minutes,total_night_calls,total_night_charge,total_intl_minutes,total_intl_calls,total_intl_charge,customer_service_calls,churn FROM public.machine_learning_customerchurn WHERE customer_service_calls > 2;''',
            destination_table='machine_learning_customerchurn',
            source_conn_id='pgdatabase',
            destination_conn_id='postgres'
    )