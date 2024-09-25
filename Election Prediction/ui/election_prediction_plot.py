import pandas as pd
import matplotlib.pyplot as plt
import sys

def plot_election_probabilities(csv_path, prediction_column='prediction'):
    # Read the CSV file without headers
    try:
        df = pd.read_csv(csv_path, header=None)
    except Exception as e:
        print(f"Error reading the CSV file: {e}")
        sys.exit(1)
    
    # Assign a column name if not present
    if df.shape[1] == 1:
        df.columns = [prediction_column]
    else:
        # Check if the specified prediction column exists
        if prediction_column not in df.columns:
            print(f"Error: The column '{prediction_column}' does not exist.")
            print(f"Available columns: {df.columns.tolist()}")
            sys.exit(1)
    
    # Validate that the prediction column contains only 0 or 1
    if not df[prediction_column].isin([0, 1]).all():
        print(f"Error: The '{prediction_column}' column must contain only 0 or 1.")
        sys.exit(1)
    
    # Count the number of predictions for each candidate
    counts = df[prediction_column].value_counts().sort_index()
    
    # Map predictions to candidate names
    candidates = {0: 'Kamala Harris', 1: 'Donald Trump'}
    counts.index = counts.index.map(candidates)
    
    # Ensure both candidates are present in the counts
    for candidate in candidates.values():
        if candidate not in counts.index:
            counts[candidate] = 0
    counts = counts.sort_index()
    
    # Calculate percentages
    total_predictions = counts.sum()
    percentages = (counts / total_predictions) * 100
    
    # Plotting the results
    plt.figure(figsize=(8, 6))
    bars = plt.bar(
        percentages.index,
        percentages.values,
        color=['red', 'blue']
    )
    plt.xlabel('Candidate', fontsize=14)
    plt.ylabel('Percentage Chance of Winning (%)', fontsize=14)
    plt.title('Election Prediction Probabilities', fontsize=16)
    plt.ylim(0, 100)
    
    # Add percentage labels on top of the bars
    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            height + 1,
            f'{height:.1f}%',
            ha='center',
            va='bottom',
            fontsize=12
        )
    
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    # Hardcoded CSV path
    csv_path = '/Users/michaelduggan/Desktop/VSCodeFiles/Projects/Election Prediction/data/processed/predictions_bool.csv'
    
    # Call the plot function with the hardcoded path
    plot_election_probabilities(csv_path)