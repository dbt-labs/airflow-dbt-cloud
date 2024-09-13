# Airflow dbt Cloud
A quick start repo for creating Airflow dags to manage your dbt Cloud jobs. 

**Please see the dbt docs on [Airflow and dbt Cloud](https://docs.getdbt.com/guides/airflow-and-dbt-cloud) for an in-depth step-by-step tutorial. Only the key concepts are included in this README.**

Please see the [dbt Cloud Airflow Provider](https://airflow.apache.org/docs/apache-airflow-providers-dbt-cloud/stable/index.html) docs for the most up-to-date details on the Airflow providers used in the example dags of this repo.

# Getting Started 
To use this repo you'll need:
1. [dbt Cloud Teams or Enterprise account](https://www.getdbt.com/pricing) (with [admin access](https://docs.getdbt.com/docs/cloud/manage-access/enterprise-permissions)) in order to create a service token.
2. [Docker Desktop](https://docs.docker.com/desktop/) installed
3. [Astro CLI](https://www.astronomer.io/docs/astro/cli/install-cli) installed. On Mac use `brew install astro`.

# Using this repo
After creating all the requisite accounts and installing Astro CLI, simply:
- Clone this repo locally: `gh repo clone dbt-labs/airflow-dbt-cloud`
- Create a [dbt Cloud service token](https://docs.getdbt.com/docs/dbt-cloud-apis/service-tokens)
- Create a [dbt Cloud job](https://docs.getdbt.com/docs/deploy/deploy-jobs#create-and-schedule-jobs)
- Start your Astro container: `astro dev start`
- Create a new dbt Cloud Airflow connection. To do this:
  - From the Airflow interface, navigate to Admin and click on Connections
  - Click on the + sign to add a new connection, then click on the drop down to search for the dbt Cloud Connection Type
  - Add in your connection details and your default dbt Cloud account id. This is found in your dbt Cloud URL after the accounts route section (`/accounts/{YOUR_ACCOUNT_ID}`)
- Update the code in the dags/ folder to use your Airflow connection, dbt account and dbt job information
- Run your first dbt Cloud Airflow DAG 🎉