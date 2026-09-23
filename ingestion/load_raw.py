import os 
from pathlib import Path

import pandas as pd
import snowflake.connector # official Snowflake connector for Python
from dotenv import load_dotenv # load environment variables from .env file
from snowflake.connector.pandas_tools import write_pandas # utility to write pandas DataFrame to Snowflake

load_dotenv() # load environment variables from .env file

# Establish connection to Snowflake using environment variables
conn = snowflake.connector.connect(
    account=os.getenv("SNOWFLAKE_ACCOUNT"), # account identifier from environment variable
    user=os.getenv("SNOWFLAKE_USER"), # username from environment variable
    password=os.getenv("SNOWFLAKE_PASSWORD"), # password from environment variable
    database=os.getenv("SNOWFLAKE_DATABASE"), # database identifier from environment variable
    schema=os.getenv("SNOWFLAKE_SCHEMA"), # schema identifier from environment variable
    warehouse=os.getenv("SNOWFLAKE_WAREHOUSE") # warehouse identifier from environment variable
)

print("Connection to Snowflake established successfully!")

# Loading all CSVs files

data_path = Path("data") # define the path to the data directory

for file_path in data_path.glob("*.csv"): # iterate over all CSV files in the data directory
    table_name = file_path.stem

    print(f"Loading {table_name}") # get the table name from the file name (without extension)
    
    df = pd.read_csv(file_path) # read CSV file into pandas DataFrame

    success, nchunks, nrows, _ = (
        write_pandas(
            conn=conn, 
            df=df, 
            table_name=table_name,
            database='RETAIL_ANALYTICS',
            schema='RAW',
            auto_create_table=True  # automatically create the table if it doesn't exist
            )
        ) # write DataFrame to Snowflake table

print(f"Data written to Snowflake successfully! Success: {success}, Number of chunks: {nchunks}, Number of rows: {nrows}")

conn.close()