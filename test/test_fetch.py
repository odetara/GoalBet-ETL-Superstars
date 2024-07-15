import os
import sys

# Adding the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from etl_modules.fetch import fetch_all_data


urls = [
        "https://www.football-data.co.uk/mmz4281/1920/E0.csv",
        "https://www.football-data.co.uk/mmz4281/1920/E2.csv",
        "https://www.football-data.co.uk/mmz4281/1920/E1.csv"
    ]

staging_dir = "./staging_dir"
fetch_all_data(urls, staging_dir)