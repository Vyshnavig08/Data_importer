from data_importer.api_client import APIClient
from data_importer.db import Database
import logging
import yaml

def main():
    # Load configuration
    with open("config/config.yaml", "r") as file:
        config = yaml.safe_load(file)

    # Initialize components
    api_client = APIClient(config["api"]["base_url"])
    database = Database()

    # Fetch and store data
    logging.info("Fetching mobile data...")
    mobile_data = api_client.fetch_mobile_data()
    if mobile_data:
        logging.info("Inserting data into the database...")
        database.insert_mobile_data(mobile_data)
        logging.info("Data insertion completed.")

if __name__ == "__main__":
    main()
