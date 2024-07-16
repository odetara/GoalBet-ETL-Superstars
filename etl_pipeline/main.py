
import os
import sys

# Adding the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from etl_modules.fetch import fetch_all_data
from etl_modules.extract_transform import extract_and_transform_data
from etl_modules.load import load_to_postgres, load_to_snowflake

def main():
    '''
    An ETL Data Pipeline That Fetch Football Data from URL , extract desired columns, 
    transform the data , and load to a Postgres DB.

    ETL Stages:

    - fetch_all_data(urls, staging_dir) : Fetches data from URL source using requests. Returns raw csv data in the staging_dir

    - extract_and_transform_data(staging_dir, columns, output_path) : Extract desired columns and transform data, 
                                                                      returns a transformed and processed data.

    - load_to_postgres(output_path,table_name) : Load transformed data from file explorer to Potsgres DB.

    '''
    urls = [
        "https://www.football-data.co.uk/mmz4281/1920/E0.csv",
        "https://www.football-data.co.uk/mmz4281/1920/E2.csv",
        "https://www.football-data.co.uk/mmz4281/1920/E1.csv"
    ]

    staging_dir = r"./staging_dir"
    fetch_all_data(urls, staging_dir)
    
    columns = ['Div', 'Date', 'Time', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG']
    output_path = r"./processed_data/transformed_data.csv"
    extract_and_transform_data(staging_dir, columns, output_path)
    
    table_name = 'goalbet_data'
    
    # Load processed and clean data to Postgres
    load_to_postgres(output_path,table_name)
    # Load processed and clean data to snowflake
    load_to_snowflake(output_path,table_name)

if __name__ == "__main__":
    main()