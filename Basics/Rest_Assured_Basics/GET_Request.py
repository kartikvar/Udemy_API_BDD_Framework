import requests

URI = "http://reqres.in/"
Path = "api/users"
URL = URI + Path

Query_Param_Get = {
    "page": 2
}

get_response = requests.get(URL, params=Query_Param_Get, verify=False)
print("Response is    --> ", get_response)
print("Status code is --> ", get_response.status_code)
assert get_response.status_code == 200
print(get_response.text)
print(get_response.json())