import requests  # Importing the requests module for handling HTTP requests
from pprint import pprint  # Importing the pprint module for pretty-printing data structures

sheety_endpoint = "https://api.sheety.co/0f5449d4104ea7aa6e4940ba68246ec3/myFlightDeals/prices"  # Setting the Sheety API endpoint

class DataManager:
    # This class is responsible for managing data retrieval and updating the Google Sheet.

    def __init__(self):
        self.destinations_data = {}  # Initializing destinations_data as an empty dictionary

    def fetch_data(self):
        response = requests.get(sheety_endpoint)  # Sending a GET request to Sheety API
        json_data = response.json()  # Extracting JSON data from the response
        self.destinations_data = json_data["prices"]  # Updating destinations_data with prices data
        return self.destinations_data  # Returning the fetched data

    # Making a PUT request to update the Google Sheet with the IATA codes
    def update_iata(self):
        for city in self.destinations_data:
            iata_code = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{sheety_endpoint}/{city['id']}", json=iata_code)  # Sending a PUT request
            # print(response.text)

