import requests  # Importing the requests module for handling HTTP requests
from datetime import datetime
from flight_data import FlightData

TEQUILA_API_KEY = "MY_API_KEY"
tequila_endpoint = "https://api.tequila.kiwi.com"

class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def get_iata(self, city_name):
        location_endpoint = f"{tequila_endpoint}/locations/query"  # Constructing the URL for location query
        headers = {"apikey": TEQUILA_API_KEY}  # Setting the API key in the headers
        location_params = {"term": city_name}  # Setting the query parameters for location search
        response = requests.get(url=location_endpoint, headers=headers, params=location_params)  # Sending a GET request
        results = response.json()["locations"]  # Extracting locations data from the response
        iata_code = results[0]["code"]  # Extracting the IATA code from the results
        return iata_code  # Returning the IATA code

    '''departure date. Use parameters date_from and date_to to define the range for the outbound flight departure.
    Example, parameters 'date_from=01/04/2021' and 'date_to=03/04/2021' mean that the departure can be anytime between the specified dates'''
    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = {"apikey": TEQUILA_API_KEY}
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 10,  # The minimal length of stay in the destination
            "nights_in_dst_to": 18,  # The maximal length of stay in the destination
            "one_for_city": 1,  # Returns the cheapest flight to every city covered by the fly_to parameter
            "max_stopovers": 1,
            "curr": "GBP"
        }

        response = requests.get(
            url=f"{tequila_endpoint}/v2/search",
            headers=headers,
            params=query,
        )

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            departure_city=data["route"][0]["cityFrom"],
            departure_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            departure_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )

        print(f"{flight_data.destination_city}: £{flight_data.price} -- Depart: {flight_data.departure_date}-{flight_data.departure_airport} -- Return: {flight_data.return_date}-{flight_data.destination_airport}")
        return flight_data

