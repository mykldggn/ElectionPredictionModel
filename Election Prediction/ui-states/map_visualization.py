# map_visualization.py
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
import folium
import pandas as pd
import io
import os

class MapVisualization(QWidget):
    def __init__(self, parent=None):
        super(MapVisualization, self).__init__(parent)
        self.view = QWebEngineView(self)
        self.load_map()

    def load_map(self):
        # Load prediction data
        df_predictions = pd.read_csv('/Users/michaelduggan/Desktop/VSCodeFiles/Projects/Election Prediction/data/processed/predictions.csv')

        # Load GeoJSON data
        us_states = os.path.abspath('/Users/michaelduggan/Desktop/VSCodeFiles/Projects/Election Prediction/data/geojson/us_states.geojson')

        # Create the map
        m = folium.Map(location=[37.8, -96], zoom_start=4)

        # Define color mapping
        party_colors = {
            'Kamala Harris': 'blue',
            'Donald Trump': 'red'
        }

        # Add the state polygons
        folium.Choropleth(
            geo_data=us_states,
            name='choropleth',
            data=df_predictions,
            columns=['state', 'predicted_winner'],
            key_on='feature.properties.name',
            fill_color='YlGn',
            fill_opacity=0.7,
            line_opacity=0.2,
            legend_name='Predicted Winner',
            highlight=True
        ).add_to(m)

        # Add interactivity
        folium.GeoJson(
            us_states,
            name='States',
            style_function=lambda feature: {
                'fillColor': party_colors.get(
                    df_predictions.set_index('state').loc[feature['properties']['name'], 'predicted_winner'],
                    'gray'
                ),
                'color': 'black',
                'weight': 1,
                'fillOpacity': 0.7,
            },
            tooltip=folium.GeoJsonTooltip(
                fields=['name'],
                aliases=['State:'],
            ),
        ).add_to(m)

        # Save map to HTML and load into QWebEngineView
        data = io.BytesIO()
        m.save(data, close_file=False)
        self.view.setHtml(data.getvalue().decode())
        self.view.setGeometry(0, 0, self.width(), self.height())

    def resizeEvent(self, event):
        self.view.resize(self.size())
