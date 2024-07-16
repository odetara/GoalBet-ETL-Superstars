
import pandas as pd
from utils.db import get_snowflake_engine, get_postgres_engine

def load_to_postgres(output_path, table_name):
    '''
    This logic loads transformed data from 'output_path' to Postgres DB using SQLalchemy engine.
    
    Parameters: 
    - output_path : path of the clean and transformed data to be read by pandas and loaded to DB
    - table_name: target table name where data is transformed is loaded.

    Return: None 
    
    '''
    # Read processed data to dataframe and write to DB
    df = pd.read_csv(output_path)

    # get the imported module for Postgres Engine
    engine = get_postgres_engine()

    # Writing to Postgres DB using the engine
    df.to_sql(table_name, engine, if_exists='append', index=False)
    print(f"{len(df)} rows of data successfully loaded to PostgreSQL table '{table_name}'")

def load_to_snowflake(output_path, table_name):
    '''
    This logic loads transformed data from 'output_path' to Snowflake DB using SQLalchemy engine.
    
    Parameters: 
    - output_path : path of the clean and transformed data to be read by pandas and loaded to DB
    - table_name: target table name where data is transformed is loaded.

    Return: None 
    
    '''
    # Read processed data to dataframe and write to DB
    df = pd.read_csv(output_path)

    # get the imported module for Snowflake Engine
    engine = get_snowflake_engine()

    # Writing to Snowflake DB using the engine
    df.to_sql(table_name, engine, if_exists='append', index=False)
    print(f"{len(df)} rows of data successfully loaded to Snowflake DW on table '{table_name}'")
