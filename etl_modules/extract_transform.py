import os
import pandas as pd

def extract_and_transform_data(staging_dir, columns, output_path):
    '''
    Extracts specified columns from all CSV files in a predefined directory 'staging_dir',
    combines that extracted data into an 'all_data' list, 
    transforms 'Date' and 'Time' columns, and saves the transformed data to an output file.

    Parameters:
    staging_dir (str): The directory containing the CSV files.
    columns (list): A list of column names to extract from each CSV file.
    output_path (str): The file path where the transformed data will be saved.

    Returns: None

    '''

    # data extraction logic for all files usung a loop
       
    all_data = []
    for file_name in os.listdir(staging_dir):

        # Iterate over each file in the directory
        file_path = os.path.join(staging_dir, file_name)
        df = pd.read_csv(file_path)
        extracted_df = df[columns]

        # Append the extracted DataFrame to the list initiated at the start of the logic
        all_data.append(extracted_df)
     
    # data cleaning and transformation 
    combined_df = pd.concat(all_data, ignore_index=True).drop_duplicates()
    combined_df['Date'] = pd.to_datetime(combined_df['Date'], format='%d/%m/%Y')
    combined_df['Time'] = pd.to_datetime(combined_df['Time'], format='%H:%M', errors='coerce').dt.time
    
    combined_df.to_csv(output_path, index=False)
    print(f"{len(combined_df)} rows of transformed data saved to {output_path}")