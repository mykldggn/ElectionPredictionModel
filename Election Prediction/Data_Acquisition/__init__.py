# data_acquisition/__init__.py

from .poll_data_scraper import get_current_polling_data
from .historical_data_downloader import download_historical_data

__all__ = ['get_current_polling_data', 'download_historical_data']
