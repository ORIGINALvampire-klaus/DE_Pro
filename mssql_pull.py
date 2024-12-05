import pyodbc
import pandas as pd
import json

# Load configuration from a JSON file
with open("config.json") as config_file:
    config = json.load(config_file)

# Connection function
def connect_to_sql_server():
    try:
        conn_str = (
            f"DRIVER={config['azure_sql']['driver']};"
            f"SERVER={config['azure_sql']['server']};"
            f"DATABASE={config['azure_sql']['database']};"
            f"UID={config['azure_sql']['username']};"
            f"PWD={config['azure_sql']['password']}"
        )
        conn = pyodbc.connect(conn_str)
        print("Connection to SQL Server was successful")
        return conn
    except pyodbc.Error as e:
        print("Error connecting to SQL Server:", e)
        return None

# Function to pull data
def pull_data_from_sql(query):
    conn = connect_to_sql_server()
    if conn is not None:
        try:
            data = pd.read_sql(query, conn)
            print("Data pulled successfully")
            return data
        except pyodbc.Error as e:
            print("Error pulling data:", e)
            return None
        finally:
            conn.close()
            print("SQL Server connection closed")


