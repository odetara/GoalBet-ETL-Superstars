from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
from snowflake.sqlalchemy import URL as URL_sn
from sqlalchemy.engine.url import URL as URL_pg


# Load postgres credentials from .env
load_dotenv(override=True)


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
    db_url = URL_pg.create(
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

def get_snowflake_engine():

    '''
    constructs a snowflake engine object for snowflake DB from .env file

    parameter: None

    Returns: 
     - snowflake-connector engine (sqlalchemy.Engine)
    '''

    # create engine for snowflake
    try:
        # Create Snowflake URL
        snowflake_url = URL_sn(
            user=os.getenv('sn_user'),
            password=os.getenv('sn_password'),
            account=os.getenv('sn_account_identifier'),
            database=os.getenv('sn_database'),
            schema=os.getenv('sn_schema'),
            warehouse=os.getenv('sn_warehouse'),
            role=os.getenv('sn_role')
        )

        # Create SQLAlchemy engine and return it
        engine = create_engine(snowflake_url)
        return engine

    except Exception as e:
        print(f"Error creating Snowflake engine: {e}")
        return None