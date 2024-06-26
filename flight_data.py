class FlightData:
    # This class represents the data structure for flight details.

    def __init__(self, price, departure_city, departure_airport, destination_city, destination_airport, departure_date, return_date):
        self.price = price  # Initializing the price attribute
        self.departure_city = departure_city  # Initializing the departure_city attribute
        self.destination_city = destination_city  # Initializing the destination_city attribute
        self.departure_airport = departure_airport  # Initializing the departure_airport attribute
        self.destination_airport = destination_airport  # Initializing the destination_airport attribute
        self.departure_date = departure_date  # Initializing the departure_date attribute
        self.return_date = return_date  # Initializing the return_date attribute

