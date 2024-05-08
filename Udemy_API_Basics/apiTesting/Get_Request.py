import json
from utilities.configurations import *
from utilities.resources import *
import requests

getURL = getConfig()["API"]["baseURI"] + APIResources.getBookingIDs
response = requests.get(getURL, verify=False)
print(response.status_code)
print(response.text)

print(response.json()[0]["bookingid"])
assert  response.status_code == 200

print(response.headers)
print(type(response.headers))

print("Content type is --> ", response.headers["Content-Type"])