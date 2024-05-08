import requests
from utilities.configurations import *
from utilities.resources import *

URL = getConfig()["API"]["authURI"] + AuthAPI.basicAuth

authBody = {
    "user": AuthAPI.username,
    "passwd": AuthAPI.password
}

response = requests.get(URL, auth=("user", "passwd") , verify=False)
print(response.status_code)
print(response.json())