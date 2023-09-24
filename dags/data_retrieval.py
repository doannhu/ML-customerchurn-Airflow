import os
from datetime import datetime
from airflow.decorators import task, dag
from airflow.providers.postgres.hooks.postgres import PostgresHook

@dag(
        dag_id="process_data",
        schedule_interval="@daily",
        start_date=datetime(2023, 9, 1),
        catchup=False
)

def ProcessData():
    @task
    def get_data():
        data_path = "/opt/airflow/dags/files/customer_churn_pred.csv"
        postgres_hook = PostgresHook(postgres_conn_id="pgdatabase")
        conn = postgres_hook.get_conn()
        cur = conn.cursor()
        with open(data_path, "r") as file:
            cur.copy_expert("COPY machine_learning_customerchurn (state,account_length,area_code,phone_number,international_plan,voice_mail_plan,number_vmail_messages,total_day_minutes,total_day_calls,total_day_charge,total_eve_minutes,total_eve_calls,total_eve_charge,total_night_minutes,total_night_calls,total_night_charge,total_intl_minutes,total_intl_calls,total_intl_charge,customer_service_calls,churn) FROM STDIN WITH CSV HEADER DELIMITER AS ',' QUOTE '\"'", file,)
            conn.commit()

    get_data()

dag = ProcessData()

if __name__ == "__main__":
    dag.test()