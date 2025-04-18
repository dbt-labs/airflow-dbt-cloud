"""
## dbt Cloud Create & Run Job Operator Example

This DAG create a new dbt job (if one does not exist with the name specified)
and then uses the DbtCloudRunJobOperator() to run the newly created job.
"""

from datetime import datetime

from airflow.models import DAG
from utils.dbt_cloud_run_job_create_operator import DbtCloudRunJobCreateOperator

import os

DEFAULT_ARGS = {
    "dbt_cloud_conn_id": os.environ.get('DBT_CLOUD_CONN_ID'),
    "account_id": os.environ.get('ACCOUNT_ID'),
    "project_id": os.environ.get('PROJECT_ID'),
    "environment_id": os.environ.get('ENV_ID')
}

with DAG(
    dag_id="dbt_cloud_run_job_create",
    default_args=DEFAULT_ARGS,
    start_date=datetime(2021, 1, 1),
    schedule_interval=None,
    catchup=False,
) as dag:

    trigger_dbt_cloud_job_run = DbtCloudRunJobCreateOperator(
        task_id="trigger_dbt_cloud_job_run",
        project_name=os.environ.get('PROJECT_NAME'),
        environment_name=os.environ.get('ENVIRONMENT_NAME'),
        job_name=os.environ.get('JOB_NAME'),
        check_interval=10,
        timeout=300,
        retry_from_failure=False,
        default_steps_on_create=["dbt build"],
    )

    trigger_dbt_cloud_job_run