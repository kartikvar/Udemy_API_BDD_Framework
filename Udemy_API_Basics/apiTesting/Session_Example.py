import requests

URL = "https://httpbin.org/basic-auth/user/passwd"

# Authentication
se = requests.session()
se.auth = ("user", "passwd")

response = se.get(URL, verify=False)
print(response.status_code)