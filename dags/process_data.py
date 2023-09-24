from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from datetime import datetime
from airflow.operators.generic_transfer import GenericTransfer

with DAG(dag_id='create_tables',
         start_date=datetime(2023, 9, 1), schedule_interval='@daily',
         catchup=False) as dag:
    create_table = PostgresOperator(
        task_id='create_MLcustomer_table',
        postgres_conn_id='postgres',
        sql='''
            CREATE TABLE IF NOT EXISTS machine_learning_customerchurn(
                state TEXT NULL,
                account_length INTEGER NULL,
                area_code INTEGER NULL,
                phone_number TEXT NULL,
                international_plan TEXT NULL,
                voice_mail_plan TEXT NULL,
                number_vmail_messages INTEGER NULL,
                total_day_minutes FLOAT NULL,
                total_day_calls INTEGER NULL,
                total_day_charge FLOAT NULL,
                total_eve_minutes FLOAT NULL,
                total_eve_calls INTEGER NULL,
                total_eve_charge FLOAT NULL,
                total_night_minutes FLOAT NULL,
                total_night_calls INTEGER NULL,
                total_night_charge FLOAT NULL,
                total_intl_minutes FLOAT NULL,
                total_intl_calls INTEGER NULL,
                total_intl_charge FLOAT NULL,
                customer_service_calls INTEGER NULL,
                churn BOOLEAN NULL
            );
        '''
    )

    create_users_table = PostgresOperator(
        task_id='create_users_table',
        postgres_conn_id='postgres',
        sql='''
            CREATE TABLE IF NOT EXISTS users(
                first_name TEXT NULL,
                last_name TEXT NULL,
                email TEXT NULL,
                street_number SMALLINT NULL,
                street_name TEXT NULL,
                surburb TEXT NULL,
                post_code INTEGER NULL,
                state TEXT NULL,
                country TEXT NULL
            );
        '''
    )

    transfer_data = GenericTransfer(
        task_id='extr_data',
        sql='''SELECT state,account_length,area_code,phone_number,international_plan,voice_mail_plan,number_vmail_messages,total_day_minutes,total_day_calls,total_day_charge,total_eve_minutes,total_eve_calls,total_eve_charge,total_night_minutes,total_night_calls,total_night_charge,total_intl_minutes,total_intl_calls,total_intl_charge,customer_service_calls,churn FROM public.machine_learning_customerchurn WHERE customer_service_calls < 2;''',
        destination_table='machine_learning_customerchurn',
        source_conn_id='pgdatabase',
        destination_conn_id='postgres',
        preoperator="TRUNCATE TABLE machine_learning_customerchurn;" ,
    )

    create_users_table >> create_table >> transfer_data
