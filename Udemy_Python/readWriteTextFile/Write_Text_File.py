file = open("D:\\Learn_Devops\\Learn_Devops_Latest\\RestAssured\\Files\\writeFile.txt", "w")
file.write("hi i m kartik")
file.write("\nmy name is kartik")

file = open("D:\\Learn_Devops\\Learn_Devops_Latest\\RestAssured\\Files\\writeFile.txt", "r")
for i in file:
    print(i)

file.close()