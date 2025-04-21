
"""
## dbt Cloud Run Job Operator Example

This DAG triggers a run of a dbt Cloud job.

Refer directly to the operator docs to for a list of acceptable arguments:
https://github.com/apache/airflow/blob/113528cbb206bbf44d04282861ed96a789bcbfbd/providers/dbt/cloud/src/airflow/providers/dbt/cloud/operators/dbt.py

"""

from datetime import datetime

from airflow.models import DAG
from airflow.providers.dbt.cloud.operators.dbt import DbtCloudRunJobOperator

import os

DEFAULT_ARGS = {
    "dbt_cloud_conn_id": os.environ.get('DBT_CLOUD_CONN_ID'),
    "account_id": os.environ.get('ACCOUNT_ID'),
}

with DAG(
    dag_id="dbt_cloud_run_job",
    default_args=DEFAULT_ARGS,
    start_date=datetime(2021, 1, 1),
    schedule_interval=None,
    catchup=False,
) as dag:

    trigger_dbt_cloud_job_run = DbtCloudRunJobOperator(
        task_id="trigger_dbt_cloud_job_run",
        job_id=os.environ.get('JOB_ID'),
        check_interval=10,
        timeout=300,
        retry_from_failure=True,
    )

    trigger_dbt_cloud_job_run
