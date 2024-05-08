import json

with open("D:\\Learn_Devops\\Learn_Devops_Latest\\RestAssured\\Files\\json_file.txt", "r") as file:
    data = json.load(file)
    print(type(data))
    print("Name is --> ", data["name"])
    print("Languages are --> ", data["languages"])
    print("First Language is --> ", data["languages"][0])
    print("Second Language is --> ", data["languages"][1])