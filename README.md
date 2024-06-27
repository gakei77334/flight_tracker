# Flight Search and Notification System
This Python script automates the process of fetching flight data, updating IATA codes for destinations, and notifying users about lower flight prices using SMS alerts.

**Key Features:**
* Data Management: Utilizes the DataManager class to fetch and manage data from a Google Sheet containing destination information.
* Flight Search: Utilizes the FlightSearch class to check available flights between a specified origin (MY_IATA) and destinations fetched from the Google Sheet.
* Automatic IATA Code Update: Checks if the IATA code for destinations is missing, updates them using the FlightSearch.get_iata() method, and updates the Google Sheet with the new data.
* Flight Price Monitoring: Searches for flights from tomorrow to six months ahead (adjustable), or for specific dates if provided, comparing current prices with previously stored lowest prices for each destination.
* Notification System: Sends SMS alerts using the NotificationManager class if a lower flight price is found compared to the stored lowest price.

**Technologies Used:**
* Python
* Google Sheets API (via DataManager)
* Flight API (via FlightSearch)
* SMS API (via NotificationManager)
