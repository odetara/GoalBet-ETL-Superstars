import os
import sys
import pandas as pd


# Adding the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from etl_modules.load import load_to_snowflake


output_path = r'C:\Users\villy\Documents\GitHub\GoalBet-ETL-Superstars\processed_data\transformed_data.csv'
table_name = 'goalbet_data'
load_to_snowflake(output_path,table_name)