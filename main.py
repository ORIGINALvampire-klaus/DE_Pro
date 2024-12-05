import logging

from data_load import load_data_to_csv
from mssql_pull import *
from trans_sq import *

if __name__ == "__main__":
    # SQL query to execute
    query = "SELECT TOP 10 * FROM [dbo].[Customers]"  # Replace with your table name
    
    # Pull data from SQL Server
    data = pull_data_from_sql(query)
    if data is not None:
        print("Raw Data:")
        print(data)

        # Transform data
        transformed_data = transform_data(data)
        if transformed_data is not None:
            print("Transformed Data:")
            print(transformed_data)

            # Load transformed data to a CSV file
            load_data_to_csv(transformed_data)
