# data_cleaning.py
import pandas as pd
import os

def clean_polling_data():
    df_polls = pd.read_csv('/Users/michaelduggan/Desktop/VSCodeFiles/Projects/Election Prediction/data/raw/current_polls.csv')

      # Print available columns to verify correct names
    print("Available columns in the DataFrame:")
    print(df_polls.columns.tolist())

    # Ensure 'candidate_a' and 'candidate_b' columns exist
    if 'Kamala Harris' in df_polls.columns and 'Donald Trump' in df_polls.columns:
        # Drop rows where either 'Kamala' or 'Trump' has missing values
        df_polls.dropna(subset=['Kamala Harris', 'Donald Trump'], inplace=True)
    else:
        print("Error: 'Kamala Harris' or 'Donald Trump' columns not found in the DataFrame.")

    return df_polls

if __name__ == '__main__':
    clean_polling_data()
