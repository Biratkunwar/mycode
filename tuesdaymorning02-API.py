#!/usr/bin/python3
"""RZFeeser | Tuesday Morning Review
Given the data contained within issnow, available from:
    
    http://api.open-notify.org/iss-now.json

Write a program that displays the current:

At, <timestamp> the iss is:
    Longitude - <longitude>
    Latitude - <latitude>
"""

# this library is necessary for sending HTTP messages
import requests

def main():
    # this is our source data
    # issnow = {"message": "success", "timestamp": 1617722139, "iss_position": {"longitude": "135.1913", "latitude": "-40.6081"}}

    # send an HTTP GET to define issnow
    issnow = requests.get("http://api.open-notify.org/iss-now.json") # this returns an HTTP 200+json
    # redefine issnow, not as a requests object, but as the JSON returned on the 200
    # converted to pythonic lists and dictionaries
    issnow = issnow.json()

    # Your code goes below here

    # grab all our values we need to display
    ts = str(issnow.get("timestamp"))                       # timestamp
    longit = issnow.get("iss_position").get("longitude")    # longitude
    latit = issnow.get("iss_position").get("latitude")      # latitude


    # display the data
    print("At, " + ts + " the iss is:")
    print("Longitude - " + longit)
    print("Latitude - " + latit)

    # you could also use f-strings to perform the same operations
    #print(f"At, {issnow.get("timestamp")} the iss is:")
    #print(f"Longitude - {issnow.get('iss_potion').get('longitude')}")
    #print(f"Longitude - {issnow.get('iss_potion').get('latitude')}")

main()
