import requests

URL = "https://rahulshettyacademy.com/"
site_cookie = {
    "visit-month": "February"
}

response = requests.get(URL, cookies=site_cookie , verify=False)
print(response.status_code)