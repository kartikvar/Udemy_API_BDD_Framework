import requests

baseURI = "https://restful-booker.herokuapp.com/"
endPoint = "booking"
URL = baseURI + endPoint

body = {
    "firstname" : "Jim",
    "lastname" : "Brown",
    "totalprice" : 111,
    "depositpaid" : False,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
}

response = requests.post(URL, json=body, verify=False)
print(response.text)