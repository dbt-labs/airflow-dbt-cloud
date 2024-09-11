
"""
## dbt Cloud Run Job Operator Example

This DAG triggers a run of a dbt Cloud job. To use, simply update the settings on lines 33-35.

Please see [Airflow dbt Cloud Operators](https://airflow.apache.org/docs/apache-airflow-providers-dbt-cloud/stable/operators.html)
for the most up-to-date information and additional explanation of how these inputs work.

Currently this operator accepts the following inputs
- check_interval: number of seconds between operator checking the job status
- timeout: maximum number of seconds that node can run before terminating
- wait_for_termination: defaults to True. Set to False to perform an asynchronous wait.
    Typically paired with the DbtCloudJobRunSensor.
    Setting `wait_for_termination` to False is a good approach for long-running dbt Cloud jobs.
- deferrable: along with wait_for_termination will control the functionality whether to poll the job status
    on the worker or defer using the Triggerer
- retry_from_failure (optional): defaults to False. Set to True to retry the run for a job from the point of failure, if the run failed.
- schema_override (optional): include this parameter to change the default build schema.
- steps_override (optional): include this parameter to change the default job steps.
- additional_run_config (optional): include this parameter to specify additional runtime configurations/overrides for the job run;
    such as threads_override, generate_docs_override, git_branch, etc.
    For a complete list of configurations, reference the [API documentation](https://docs.getdbt.com/dbt-cloud/api-v2#/).

"""

from datetime import datetime

from airflow.models import DAG
from airflow.providers.dbt.cloud.operators.dbt import DbtCloudRunJobOperator

### Update these ids to match your account ###
DBT_CLOUD_CONN_ID = "dbt_cloud"
ACCOUNT_ID = "222529"
JOB_ID = "710606"

with DAG(
    dag_id="dbt_cloud_run_job",
    default_args={"dbt_cloud_conn_id": DBT_CLOUD_CONN_ID, "account_id": ACCOUNT_ID},
    start_date=datetime(2021, 1, 1),
    schedule_interval=None,
    catchup=False,
) as dag:

    trigger_dbt_cloud_job_run = DbtCloudRunJobOperator(
        task_id="trigger_dbt_cloud_job_run",
        job_id=JOB_ID,
        check_interval=10,
        timeout=300,
        retry_from_failure=True,
    )

    trigger_dbt_cloud_job_run