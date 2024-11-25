import requests
import logging

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def fetch_mobile_data(self):
        try:
            response = requests.get(self.base_url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logging.error(f"Error fetching data: {e}")
            return None
