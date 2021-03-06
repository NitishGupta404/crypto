import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
import json
import requests
import schedule
import time


print("Started...")
def crypto():
    k=requests.get("https://api.nomics.com/v1/currencies/ticker?key=05e4f406284751d38ccf58d14d61ace44a6c8741&ids=ADA&interval=1h,1d&convert=INR&per-page=100&page=1%22").text
    coindata=json.loads(k)
    cardano=coindata[0]['price']

    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    account_sid = "ACf8591d41773a5c4c3e70a88cf9e97524"
    auth_token = "9b086b5bd5a727261a69f666be311dab"

    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages.create(
                                      body='Current cardano price is '+cardano,
                                      from_='whatsapp:+14155238886',
                                      to='whatsapp:'
                                  )
    # print(message.sid)
print("Running...")
schedule.every().hour.do(crypto)
while True:
    schedule.run_pending()
    time.sleep(1)




# twilio api calls will now work from behind the proxy:
