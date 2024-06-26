from twilio.rest import Client  # Importing the Client class from twilio.rest module

TWILIO_SID = "MY_TWILIO_SID"  # Setting Twilio SID
TWILIO_AUTH_TOKEN = "MY_TWILIO_AUTH_TOKEN"  # Setting Twilio authentication token
TWILIO_VIRTUAL_NUMBER = "+447000000000"  # Setting Twilio virtual number
TWILIO_VERIFIED_NUMBER = "+447111111111"  # Setting Twilio verified number

class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)  # Creating an instance of the Twilio Client class

    def send_sms(self, message):
        message = self.client.messages \
            .create(
                body=message,
                from_=TWILIO_VIRTUAL_NUMBER,
                to=TWILIO_VERIFIED_NUMBER
        )
        print(f"Sending txt message -- {message.sid}")  # Printing the SID of the sent message
