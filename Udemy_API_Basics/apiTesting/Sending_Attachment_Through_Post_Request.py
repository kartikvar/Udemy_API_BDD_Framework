import requests

file = {"file": open("C:\\Users\\kbudakoti\\Desktop\\Dehradun\\Dehradun.jpeg", "rb")}
response = requests.post("https://petstore.swagger.io/v2/pet/9843217/uploadImage", files=file, verify=False)

print(response.text)
print(response.json())