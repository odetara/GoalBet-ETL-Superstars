import os
import pandas as pd
from sqlalchemy.engine.url import URL
from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError
from dotenv import load_dotenv

def get_postgres_engine():
    """
    Creates and returns a SQLAlchemy engine for connecting to a PostgreSQL database.
    """
    load_dotenv(override=True)
    
    # Fetch the connection parameters from environment variables
    username = os.getenv('pg_user')
    password = os.getenv('pg_password')
    host = os.getenv('pg_host', 'localhost')
    port = os.getenv('pg_port', '5432')
    database = os.getenv('pg_dbname')
    
    # Log the connection parameters (excluding the password for security)
    print(f"Attempting to connect to PostgreSQL database with the following parameters:")
    print(f"User: {username}")
    print(f"Host: {host}")
    print(f"Port: {port}")
    print(f"Database: {database}")
    
    # Create the connection URL
    db_url = URL.create(
        drivername='postgresql+psycopg2',
        username=username,
        password=password,
        host=host,
        port=port,
        database=database
    )
    
    # Create the SQLAlchemy engine
    engine = create_engine(db_url)
    
    # Return the engine
    return engine

def test_connection(engine):
    """
    Tests the connection to the PostgreSQL database by executing a simple query.
    """
    try:
        # Connect to the database and execute a simple query
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            print("Connection successful! Test query result:", result.scalar())
    except OperationalError as e:
        print("Connection failed!")
        print(str(e))

def load_data_to_postgres(output_path, table_name):
    """
    Loads data from a CSV file to a PostgreSQL table.

    Parameters:
    output_path (str): The path to the CSV file.
    table_name (str): The name of the target PostgreSQL table.
    """
    # Read data from CSV
    df = pd.read_csv(output_path)
    
    
    engine = get_postgres_engine()
    
    # Test the connection
    test_connection(engine)
    
    try:
        df.to_sql(table_name, engine, if_exists='append', index=False)
        print(f"{len(df)} rows of data successfully loaded to PostgreSQL table '{table_name}'")
    except Exception as e:
        print("Failed to load data to PostgreSQL table")
        print(str(e))

if __name__ == "__main__":
    output_path = r"./processed_data/transformed_data.csv"
    table_name = 'goalbet_data'
    
    # Load data to PostgreSQL
    load_data_to_postgres(output_path, table_name)
