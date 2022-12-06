
from twilio.rest import Client

account_sid = 'AC7c011252b7c1d265887b003270663deb'
auth_token = 'a1eb2a039fcd54d1f3f37ddf9ecad0e4'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Hi there',
                              from_='+15017122661',
                              to='xxxx'
                          )

print(message.sid)
