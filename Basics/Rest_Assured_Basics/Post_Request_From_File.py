import json
import jsonpath
import requests

URL = "https://reqres.in/api/users"
file = open("D:\\Learn_Devops\\Learn_Devops_Latest\\RestAssured\\RestAssured\\payload.json", "r")
payload = json.loads(file.read())

response = requests.post(URL, data=payload, verify=False)
print("------------------------------------ Printing payload ------------------------------------")
print(payload)
print("------------------------------------ Printing Status Code ------------------------------------")
print(response.status_code)
print("------------------------------------ Printing response in text ------------------------------------")
print(response.text)
print("------------------------------------ Printing response in json ------------------------------------")
print(response.json())

assert response.status_code == 201
print("------------------------------------ Printing the name ------------------------------------")
name = jsonpath.jsonpath(response.json(), "name")
print("Name is --> ", name)