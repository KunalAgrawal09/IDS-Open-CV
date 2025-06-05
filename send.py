from twilio.rest import Client
account_sid = 'AC622be265cdafc9c795a034a9098b1fd8'
auth_token = '56c2bcc174c00f833622dcd3510a0c16'
client = Client(account_sid, auth_token)
def sendSms():
  message = client.messages.create(
  from_= '+19414019205',
  body ='ALERT',
  to='+919955103131'
  )
  print(message.sid)