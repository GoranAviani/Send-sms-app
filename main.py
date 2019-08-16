from twilio.rest import Client
from credentials.credentials import my_account_sid, my_auth_token, my_telephone, my_service_telephone

account_sid = my_account_sid
auth_token = my_auth_token

client1 = Client(account_sid, auth_token)

message1 = client1.messages \
                .create(
                     body="Pozdrav od Gorana.",
                     from_= my_service_telephone,
                     to=my_telephone
                 )


print(message1.sid)