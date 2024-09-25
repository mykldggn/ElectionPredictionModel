# model_prediction.py
import pandas as pd
import joblib
import os
import sys

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Data_Processing.feature_engineering import engineer_features

def predict_election():
    # Engineer features for the current data
    input_path = '/Users/michaelduggan/Desktop/VSCodeFiles/Projects/Election Prediction/data/raw/current_polls.csv'
    output_path = '/Users/michaelduggan/Desktop/VSCodeFiles/Projects/Election Prediction/data/processed/features.csv'
    df = engineer_features(input_path, output_path)

    # Load the model and required columns
    model_dir = '/Users/michaelduggan/Desktop/VSCodeFiles/Projects/Election Prediction/data/models'
    model = joblib.load(os.path.join(model_dir, 'election_model.pkl'))
    required_columns = joblib.load(os.path.join(model_dir, 'feature_columns.pkl'))

    # Ensure all required columns are present
    for col in required_columns:
        if col not in df.columns:
            if col.endswith('_share'):
                base_col = col.replace('_share', '')
                if base_col in df.columns:
                    df[col] = df[base_col] / 100  # Convert percentage to share
            else:
                df[col] = 0  # or some other appropriate default value

    # Select only the required columns for prediction
    X = df[required_columns]

    # Make predictions
    predictions = model.predict(X)
    
    # Map predictions to candidate names
    prediction_mapping = {0: 'Kamala Harris', 1: 'Donald Trump'}
    df['predicted_winner'] = [prediction_mapping.get(pred, pred) for pred in predictions]

    # Save predictions
    predictions_path = '/Users/michaelduggan/Desktop/VSCodeFiles/Projects/Election Prediction/data/processed/predictions.csv'
    df['predicted_winner'].to_csv(predictions_path, index=False)
    print(f"Predictions saved to {predictions_path}")

if __name__ == '__main__':
    predict_election()

