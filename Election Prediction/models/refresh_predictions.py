# refresh_predictions.py

import pandas as pd
import os
import sys

def refresh_data(input_path, output_path):
    
    # Define the mapping from candidate names to boolean values
    mapping = {
        'Kamala Harris': 0,
        'Donald Trump': 1
    }
    
    # Check if the input file exists
    if not os.path.exists(input_path):
        print(f"Error: The file '{input_path}' does not exist.")
        sys.exit(1)
    
    try:
        # Read the predictions CSV
        df = pd.read_csv(input_path)
    except Exception as e:
        print(f"Error reading '{input_path}': {e}")
        sys.exit(1)
    
    # Ensure the 'predicted_winner' column exists
    if 'predicted_winner' not in df.columns:
        print("Error: The input CSV does not contain a 'predicted_winner' column.")
        sys.exit(1)
    
    # Map the candidate names to boolean values
    df['predicted_winner_b'] = df['predicted_winner'].map(mapping)
    
    # Check for any unmapped values
    if df['predicted_winner_b'].isnull().any():
        unmapped = df[df['predicted_winner_b'].isnull()]['predicted_winner'].unique()
        print(f"Error: Found unmapped candidate names: {unmapped}")
        sys.exit(1)
    
    # Select only the boolean column for the output
    df_bool = df[['predicted_winner_b']]


    try:
        # Save the converted predictions to the output CSV
        df_bool.to_csv(output_path, index=False, header=False)
        print(f"Boolean predictions saved to '{output_path}'.")
    except Exception as e:
        print(f"Error saving to '{output_path}': {e}")
        sys.exit(1)

if __name__ == '__main__':
    # Define the input and output paths
    input_path = '/Users/michaelduggan/Desktop/VSCodeFiles/Projects/Election Prediction/data/processed/predictions.csv'
    output_path = '/Users/michaelduggan/Desktop/VSCodeFiles/Projects/Election Prediction/data/processed/predictions_bool.csv'
    
    # Convert the predictions
    refresh_data(input_path, output_path)
