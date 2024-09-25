# feature_engineering.py
import pandas as pd
import os

def engineer_features(input_file, output_file):
    # Load the data
    df = pd.read_csv(input_file)

    # Perform feature engineering
    # Example: Calculate poll margin
    df['poll_margin'] = df['Kamala Harris'] - df['Donald Trump']

    # Use 'end_date' as the primary date for calculations
    df['date'] = pd.to_datetime(df['end_date'], errors='coerce')

    # Calculate days to election
    election_date = pd.to_datetime('2024-11-05')
    df['days_to_election'] = (election_date - df['date']).dt.days

    # Save the engineered features
    df.to_csv(output_file, index=False)
    print(f"Feature engineered, data saved to {output_file}")

    return df

if __name__ == '__main__':
    input_file = '/Users/michaelduggan/Desktop/VSCodeFiles/Projects/Election Prediction/data/raw/current_polls.csv'
    output_file = '/Users/michaelduggan/Desktop/VSCodeFiles/Projects/Election Prediction/data/processed/features.csv'
    engineer_features(input_file, output_file)
