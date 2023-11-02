
# Real time End-to-end machine learning project to predict customer churn (DevOps and Data Engineering)

 - End-to-end machine learning project to predict customer churn using different models: Random Forest, Naive Bayes, AdaBoost and XGBoost. 

 - The customer data is loaded over API through Django web app or through a batch (csv files) and saved in Postgres database, then the prediction result can be returned via Rest API. 

 - The system uses 2 databases for raw data and transformed data. 

 - The data in the first Postgres database can be extracted to the second Postgres database and this is scheduled and managed by a pipeline in Airflow.

 - The tasks in Airflow is executed by Celery Executor Cluster (with 2 workers) with Redis message broker. 

 - The data is validated and transformed before storing into database. 

 - The project is Test-Driven Development approach (use unit testing), run on Docker Containers.

 - The project uses Github Action as the Continuous Integration (CI).



