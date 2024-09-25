# historical_data_downloader.py
import pandas as pd
import requests
import os

import pandas as pd

def download_historical_data():
    # Path to the local CSV file
    local_file_path = '/Users/michaelduggan/Desktop/VSCodeFiles/Projects/Election Prediction/data/raw/historical_elections.csv'

    try:
        # Load the data from the local CSV file into a pandas DataFrame
        df_historical = pd.read_csv(local_file_path)

        # Print the first few rows of the DataFrame to verify
        print(df_historical.head())
        print("Historical data loaded successfully.")
    except FileNotFoundError as e:
        print(f"Error: File not found - {e}")
    except pd.errors.ParserError as e:
        print(f"Error: Failed to parse CSV - {e}")

if __name__ == '__main__':
    download_historical_data()
