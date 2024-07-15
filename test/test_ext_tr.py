import os
import sys

# Adding the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from etl_modules.extract_transform import extract_and_transform_data

staging_dir = './staging_dir'
columns = ['Div', 'Date', 'Time', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG']
output_path = './processed_data/transformed_data.csv'


extract_and_transform_data(staging_dir, columns, output_path)