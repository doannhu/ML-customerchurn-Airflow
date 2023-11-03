
# Real time End-to-end machine learning project to predict customer churn (DevOps and Data Engineering)

 - :dependabot: End-to-end machine learning project to predict customer churn using different models: Random Forest, Naive Bayes, AdaBoost and XGBoost. 

 - :point_right: The customer data is loaded over API through Django web app or through a batch (csv files) and saved in Postgres database, then the prediction result can be returned via Rest API. 

 - :wave: The system uses 2 databases for raw data and transformed data. 

 - :monkey_face: The data in the first Postgres database can be extracted to the second Postgres database and this is scheduled and managed by a pipeline in Airflow.

 - :unicorn: The tasks in Airflow is executed by Celery Executor Cluster (with 2 workers) with Redis message broker. 

 - :writing_hand: The data is validated and transformed before storing into database. 

 - :koala: The project is Test-Driven Development approach (use unit testing), run on Docker Containers.

 - :octocat: The project uses Github Action as the Continuous Integration (CI).



