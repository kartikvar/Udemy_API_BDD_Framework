import requests

URI = "http://reqres.in/"
Path = "api/users/2"
URL = URI + Path

delete_response = requests.delete(URL, verify=False)
print("Response is    --> ", delete_response)
print("Status code is --> ", delete_response.status_code)
assert delete_response.status_code == 204
