from datetime import datetime, timedelta
from data_manager import DataManager  # Importing the DataManager class from data_manager module
from flight_search import FlightSearch  # Importing the FlightSearch class from flight_search module
from notification_manager import NotificationManager

MY_IATA = "LON"

data_manager = DataManager()  # Creating an instance of the DataManager class
flight_search = FlightSearch()  # Creating an instance of the FlightSearch class
notification_manager = NotificationManager()  # Creating an instance of the NotificationManager class

sheet_data = data_manager.fetch_data()  # Fetching data using the fetch_data method of DataManager
sheet_data = data_manager.fetch_data()

if sheet_data[0]["iataCode"] == "":  # Checking if the IATA code of the first row is empty
    for row in sheet_data:  # Loop through each row in sheet_data and update the IATA codes
        row["iataCode"] = flight_search.get_iata(row["city"])  # For each row, update the "iataCode" attribute by calling the get_iata method from the FlightSearch class
    data_manager.destinations_data = sheet_data  # Updating destinations_data with modified sheet_data
    data_manager.update_iata()  # Updating the Google Sheet with the new IATA codes by calling the update_iata method

'''Use for larger date range'''
tomorrow = datetime.now() + timedelta(days=1)  # Calculating the date for tomorrow
six_months_from_today = datetime.now() + timedelta(days=(6*30))  # Calculating the date six months from today

'''Use for SPECIFIC DATES'''
# tomorrow = datetime(2024, 3, 11)
# six_months_from_today = datetime(2024, 3, 13)

for destination in sheet_data:
    flight = flight_search.check_flights(
        MY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_months_from_today
    )
    '''Send a text msg if a lower price is found'''
    # if flight.price < destination["lowestPrice"]:
    #     notification_manager.send_sms(
    #         message=f"Low price alert! Only £{flight.price} to fly from {flight.departure_city}-{flight.departure_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.departure_date} to {flight.return_date}."
    #     )
