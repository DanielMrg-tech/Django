from twilio.rest import Client
from backend.private_settings import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN


def send_whatsapp_message(to_number, message):
    client = Client(TWILIO_AUTH_TOKEN, TWILIO_ACCOUNT_SID)
    client.messages.create(message, to_number, 'whatsapp:{}'.format(client) ,from_='whatsapp:+0755847226')