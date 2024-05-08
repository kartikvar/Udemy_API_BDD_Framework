import requests

URI = "http://reqres.in/"
Path = "api/users"
URL = URI + Path

Data_Post = {
    "name": "ashish",
    "job": "vella"
}
post_response = requests.post(URL, data=Data_Post, verify=False)
print("Response is    --> ", post_response)
print("Status code is --> ", post_response.status_code)
assert post_response.status_code == 200
print(post_response.text)