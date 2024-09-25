# model_training.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import classification_report
import joblib
import os

def train_model():
    # Load your data
    df = pd.read_csv('/Users/michaelduggan/Desktop/VSCodeFiles/Projects/Election Prediction/data/raw/current_polls.csv')

    # Ensure required columns exist
    required_columns = ['Kamala Harris', 'Donald Trump']
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Required column '{col}' not found in the DataFrame.")

    # Create 'winner' column based on poll percentages
    df['winner'] = df.apply(
        lambda row: 'Kamala Harris' if row['Kamala Harris'] > row['Donald Trump'] else (
            'Donald Trump' if row['Donald Trump'] > row['Kamala Harris'] else 'Tie'
        ),
        axis=1
    )

    # Optionally, remove rows where there's a tie
    df = df[df['winner'] != 'Tie']

    # Now you can proceed with defining X and y
    X = df[['Kamala Harris', 'Donald Trump']]
    y = df['winner']

    # Initialize and train the model
    model = GradientBoostingClassifier()
    model.fit(X, y)

     # Define the directory path
    model_dir = '/Users/michaelduggan/Desktop/VSCodeFiles/Projects/Election Prediction/data/models'
    
    # Ensure the directory exists
    os.makedirs(model_dir, exist_ok=True)
    
    # Save the trained model and feature columns
    joblib.dump(model, os.path.join(model_dir, 'election_model.pkl'))
    joblib.dump(required_columns, os.path.join(model_dir, 'feature_columns.pkl'))

    print(f"Model trained and saved in {model_dir}")

if __name__ == '__main__':
    train_model()
