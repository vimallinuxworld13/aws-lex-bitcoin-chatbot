"""
Lexbot Lambda handler.
"""
from urllib.request import Request, urlopen
import json

def get_bitcoin_price(date):
    print('get_bitcoin_price, date = ' + str(date))
    request = Request('https://rest.coinapi.io/v1/ohlcv/BITSTAMP_SPOT_BTC_USD/latest?period_id=1DAY&limit=1&time_start={}'.format(date))
    request.add_header('X-CoinAPI-Key', '73034021-0EBC-493D-8A00-E0F138111F41')
    response = json.loads(urlopen(request).read())
    return response[0]['price_close']
    
def lambda_handler(event, context):
    print('received request: ' + str(event))
    date_input = event['currentIntent']['slots']['Date']
    btc_price = get_bitcoin_price(date_input)
    response = {
        "dialogAction": {
            "type": "Close",
            "fulfillmentState": "Fulfilled",
            "message": {
              "contentType": "SSML",
              "content": "Bitcoin's price was {price} dollars".format(price=btc_price)
            },
        }
    }
    print('result = ' + str(response))
    return response
