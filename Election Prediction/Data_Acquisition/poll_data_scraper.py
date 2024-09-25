# poll_data_scraper.py
import os
import pandas as pd
from datetime import datetime

def get_current_polling_data():
    # URL to FiveThirtyEight's presidential polls dataset
    csv_url = 'https://projects.fivethirtyeight.com/polls-page/data/president_polls.csv'

    # Load the data into a DataFrame
    df = pd.read_csv(csv_url)

    # Convert 'end_date' to datetime
    df['end_date'] = pd.to_datetime(df['end_date'])

    # Define the cutoff date (August 19, 2024)
    cutoff_date = datetime(2024, 8, 19)

    # Filter for 2024 general election presidential polls before the cutoff date
    df_filtered = df[
        (df['cycle'] == 2024) &
        (df['office_type'] == 'U.S. President') &
        (df['stage'] == 'general') &
        (df['state'].isna()) &
        (df['end_date'] > cutoff_date)
    ]

    # List of candidates we're interested in
    candidates_of_interest = ['Kamala Harris', 'Donald Trump']

    # Check available candidate names
    available_candidates = df_filtered['candidate_name'].unique()
    print("Available candidates:", available_candidates)


    # Group by 'poll_id' and collect the list of candidate names in each poll
    poll_candidates = df_filtered.groupby('poll_id')['candidate_name'].agg(list).reset_index()

    # Identify polls that include both Kamala Harris and Donald Trump
    polls_with_both_candidates = poll_candidates[
        poll_candidates['candidate_name'].apply(
            lambda x: all(candidate in x for candidate in candidates_of_interest)
        )
    ]['poll_id']

    # Filter the DataFrame to include only polls with both candidates
    df_candidates = df_filtered[df_filtered['poll_id'].isin(polls_with_both_candidates)]

    # Pivot the DataFrame to have candidates as columns
    df_pivot = df_candidates.pivot_table(
        index=['poll_id', 'pollster', 'start_date', 'end_date', 'sample_size', 'population'],
        columns='candidate_name',
        values='pct'
    ).reset_index()

    # Keep only the columns we're interested in
    df_pivot = df_pivot[
        ['poll_id', 'pollster', 'start_date', 'end_date', 'sample_size', 'population', 'Kamala Harris', 'Donald Trump']
    ]

    # Save the data
    output_dir = '/Users/michaelduggan/Desktop/VSCodeFiles/Projects/Election Prediction/data/raw'
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, 'current_polls.csv')
    df_pivot.to_csv(output_file, index=False)
    print(f"Polling data saved to {output_file}")

    return df_pivot

if __name__ == '__main__':
    df_polls = get_current_polling_data()
    if not df_polls.empty:
        print(df_polls.head())
    else:
        print("No polling data found for the specified criteria.")


