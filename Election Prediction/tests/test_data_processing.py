# test_data_processing.py
import unittest
import pandas as pd
import sys
import os

# Add the project root directory to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
sys.path.append(project_root)

from Data_Processing.data_cleaning import clean_polling_data
from ui.map_visualization import MapVisualization

class TestDataProcessing(unittest.TestCase):
    def setUp(self):
        # Create a sample DataFrame for testing
        self.sample_data = pd.DataFrame({
            'candidate_a': [45, 48, None, 52],
            'candidate_b': [50, 47, 49, None],
            'date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04']
        })

    def test_clean_polling_data(self):
        cleaned_df = clean_polling_data(self.sample_data)
        
        # Check if null values are removed
        self.assertFalse(cleaned_df.isnull().values.any())
        
        # Check if expected columns are present
        self.assertIn('candidate_a', cleaned_df.columns)
        self.assertIn('candidate_b', cleaned_df.columns)
        self.assertIn('date', cleaned_df.columns)
        
        # Check if data types are correct
        self.assertEqual(cleaned_df['candidate_a'].dtype, 'float64')
        self.assertEqual(cleaned_df['candidate_b'].dtype, 'float64')
        self.assertEqual(cleaned_df['date'].dtype, 'datetime64[ns]')
        
        # Check if the number of rows is correct (2 rows should be removed due to NaN values)
        self.assertEqual(len(cleaned_df), 2)

    def test_map_visualization(self):
        # Your test cases here
        pass

if __name__ == '__main__':
    unittest.main()
