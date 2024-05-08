import csv

with open("D:\\Learn_Devops\\Learn_Devops_Latest\\RestAssured\\RestAssured\\Udemy_Python\\csvFile\\file.csv", "r") as file:
    csvReader = csv.reader(file)

    name = []
    job = []

    for rows in csvReader:
        print(rows)
        name.append(rows[0])
        job.append(rows[1])

print(name)
print("Printing Sammi --> ", name[2])
print(job)

with open("D:\\Learn_Devops\\Learn_Devops_Latest\\RestAssured\\RestAssured\\Udemy_Python\\csvFile\\file.csv", "a") as file:
    csvWriter = csv.writer(file)
    csvWriter.writerow(["Kartik", "Hero"])