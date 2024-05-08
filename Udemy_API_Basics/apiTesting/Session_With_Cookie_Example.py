import requests

se = requests.session()
se.cookies.update({"new name": "new yoyo"})
# above example shows to include cookies by session

response = se.get("https://httpbin.org/cookies", cookies={"name": "yoyo"}, verify=False)
print(response.text)