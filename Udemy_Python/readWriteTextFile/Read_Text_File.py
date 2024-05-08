file = open("D:\\Learn_Devops\\Learn_Devops_Latest\\RestAssured\\Files\\readFile.txt", "r")

print(file.readline())

for i in file:
    print(i)

file.close()