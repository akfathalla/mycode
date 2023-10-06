#!/usr/bin/env python3

""" Returning the location of the ISS in Latitude/Longitude"""

import requests

URL = "http://api.open-notify.org/iss-now.json"
def main():
    resp = requests.get(URL).json()
    print(resp)
    print("Current location of the ISS is:\nlonig:", resp["iss_position"]["longitude"], "\nLatitude:", resp["iss_position"]["latitude"])

if __name__ == "__main__":
    main()
