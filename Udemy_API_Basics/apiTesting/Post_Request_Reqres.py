import requests

baseURI = "https://reqres.in/"
endPoint = "api/users"
URL = baseURI + endPoint

body = {
    "name": "morpheus",
    "job": "leader"
}

response = requests.post(URL, data=body, verify=False)
print(response.text)