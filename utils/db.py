from sqlalchemy import create_engine, exc
from dotenv import load_dotenv
import os
from snowflake.sqlalchemy import URL

# Load postgres credentials from .env
load_dotenv(override=True)


def get_postgres_engine():
    '''
    constructs a SQLalchemy engine object for postgres DB from .env file

    parameter: None

    Returns: 
     - sqlalchemy engine (sqlalchemy.engine.Engine)
    '''
    driver = 'postgresql+psycopg2'
    user = os.getenv('pg_user')
    password = os.getenv('pg_password')
    host = os.getenv('pg_host')
    port = os.getenv('pg_port')
    dbname = os.getenv('pg_dbname')

    connection_string = f'{driver}://{user}:{password}@{host}:{port}/{dbname}'
    engine = create_engine(connection_string)
    
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
        snowflake_url = URL(
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