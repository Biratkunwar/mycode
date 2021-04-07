#!/usr/bin/python3
"""RZFeeser | BitCoin Price Tracker - USD
Tracking price of BTC to USD via:
    https://api.coindesk.com/v1/bpi/currentprice.json"""

# import requests to perform HTTP GETs and capture 200 repsonses
import requests

def main():
    # define API as variable
    api = "https://api.coindesk.com/v1/bpi/currentprice.json"

    # make HTTP GET request, and capture response
    r = requests.get(api)

    # strip the JSON off the 200 response object and map to new variable
    btcdata = r.json()

    # open a file we can write to (not overwrite)
    with open("btcPrice.data", "a") as btc:
        #btc.write() # this would work just like the line below
        #print("this goes into the file", file=btc)

        # write current timestamp & BTC to USD price from captured data
        #print(btcdata.get("time").get("updated"), file=btc)
        #print(btcdata.get("bpi").get("USD").get("rate"), file=btc)
        
        time = btcdata.get("time").get("updated")
        rate = btcdata.get("bpi").get("USD").get("rate")

        btc.write(f"{time} - {rate}\n")

    # close file


main()
