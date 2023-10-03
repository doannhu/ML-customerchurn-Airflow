FROM apache/airflow:2.7.1

ADD airflow_img_requirements.txt .

RUN pip install apache-airflow==${AIRFLOW_VERSION} -r airflow_img_requirements.txt