from twilio.rest import Client
from flight_data import FlightData


class NotificationManager:

    def __init__(self, twilio_id, twilio_token, from_number, to_number) -> None:

        self.client = Client(twilio_id, twilio_token)

        self.from_num = from_number
        self.to_num = to_number

    def generate_message(self, deal: FlightData) -> str:

        text = f"Low price alert! Only {deal.price}GBP to fly from {deal.dept_cname}-{deal.dept_airport} to {deal.dest_cname}-{deal.dest_airport}, from {deal.travel_date} to {deal.return_date}."

        return text

    def good_deals_sms(self, deals, sheet) -> None:

        lut = {city['iataCode']: city['lowestPrice'] for city in sheet}

        for deal in deals:
            
            if deal is None:
                continue

            elif deal.price <= lut[deal.dest_ccode]:

                message_body = self.generate_message(deal)

                message = self.client.messages.create(
                    body=message_body,
                    from_=self.from_num,
                    to=self.to_num
                )

                print(message.sid)

    #This class is responsible for sending notifications with the deal flight details.
