import json

with open("D:\\Learn_Devops\\Learn_Devops_Latest\\RestAssured\\Files\\json_file.txt", "r") as file:
    dic = json.load(file)

with open("D:\\Learn_Devops\\Learn_Devops_Latest\\RestAssured\\Files\\json_file1.txt", "r") as file1:
    dic1 = json.load(file1)
    assert dic == dic1
    # since data is different, above assertion will show error