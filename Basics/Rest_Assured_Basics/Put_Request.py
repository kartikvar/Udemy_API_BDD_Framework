import requests

URI = "http://reqres.in/"
Path = "api/users/2"
URL = URI + Path

Data_Put = {
    "name": "ashish",
    "job": "bada vella"
}
put_response = requests.put(URL, data=Data_Put, verify=False)
print("Response is    --> ", put_response)
print("Status code is --> ", put_response.status_code)
assert put_response.status_code == 200
print(put_response.text)
print(put_response.json())
