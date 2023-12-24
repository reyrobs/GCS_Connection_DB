from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from airflow.operators.python import get_current_context
import psycopg2
from extract import *
import sqlite3
import numpy as np
import pandas as pd

def extract_from_sqlite(database_file, table_name):
    """
    Extract data from a SQLite database.

    Parameters:
    - database_file (str): The path to the SQLite database file.
    - table_name (str): The name of the table to extract data from.

    Returns:
    - list: A list of tuples containing the extracted data.
    """

    # Connect to SQLite database
    conn = sqlite3.connect(database_file)

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    try:
        # Execute a SELECT query to extract data from the specified table
        query = f"SELECT * FROM {table_name};"
        # query = f"SELECT * FROM {table_name} ORDER BY ROWID ASC LIMIT 1;"
        cursor.execute(query)
        # Fetch the data
        data = cursor.fetchall()

        return data

    except sqlite3.Error as e:
        # Handle any errors that may occur during the extraction
        print(f"Error: {e}")
        return None

    finally:
        # Close the cursor and connection
        cursor.close()
        conn.close()

# def transform():
#     pass
#
# def load():
#     pass
#
# default_args = {
#     'owner': 'your_name',
#     'start_date': datetime(2023, 1, 1),
#     'retries': 1,
#     'retry_delay': timedelta(minutes=5),
# }
#
# dag = DAG(
#     'etl_pipeline',
#     default_args=default_args,
#     description='A simple ETL pipeline',
#     schedule_interval='@daily',
# )
#
# extract_task = PythonOperator(
#     task_id='extract',
#     python_callable=extract,
#     dag=dag,
# )
#
# transform_task = PythonOperator(
#     task_id='transform',
#     python_callable=transform,
#     dag=dag,
# )
#
# load_task = PythonOperator(
#     task_id='load',
#     python_callable=load,
#     dag=dag,
# )

if __name__ == '__main__':
    data = extract_from_sqlite('test1.db', 'e_commerce')
    column_names = get_col_names('test1.db', 'e_commerce')
    df1 = pd.DataFrame(np.array(data), columns=column_names)