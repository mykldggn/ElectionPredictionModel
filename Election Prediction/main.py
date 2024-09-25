# main.py (or any other script)

from Data_Acquisition import get_current_polling_data
from Data_Processing import clean_polling_data, engineer_features 
from models import train_model, predict_election, refresh_data
from ui import election_prediction_plot
# Data Acquisition
df_polls = get_current_polling_data()

# Data Processing
df_clean = clean_polling_data()
input_file = '/Users/michaelduggan/Desktop/VSCodeFiles/Projects/Election Prediction/data/raw/current_polls.csv'
output_file = '/Users/michaelduggan/Desktop/VSCodeFiles/Projects/Election Prediction/data/processed/features.csv'
df_features = engineer_features(input_file, output_file)
# Modeling
train_model()
predict_election()
input_path = '/Users/michaelduggan/Desktop/VSCodeFiles/Projects/Election Prediction/data/processed/predictions.csv'
output_path = '/Users/michaelduggan/Desktop/VSCodeFiles/Projects/Election Prediction/data/processed/predictions_bool.csv'
refresh_data(input_path, output_path)
# Launch UI
#app = election_prediction_plot()
#app.run()
