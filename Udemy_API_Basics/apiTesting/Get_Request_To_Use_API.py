import requests

baseURI = "http://216.10.245.166/"
endPoint = "Library/GetBook.php"
URL = baseURI + endPoint
parameter = {
    "AuthorName": "rahul"
}

response = requests.get(URL, params=parameter, verify=False)
print(response.status_code)
print(response.text)

# https://drive.google.com/file/d/18FC3jDnsOol9zn3_KGSrjg35a4unpiSG/view