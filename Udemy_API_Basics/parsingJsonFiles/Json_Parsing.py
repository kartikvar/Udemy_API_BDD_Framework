import json

courses = '{"name": "Rahul", "languages": ["java","python"]}'

# Loads method parse json string and it returns dictionary
dic_courses = json.loads(courses)
print(type(dic_courses))
print("Name is --> ", dic_courses["name"])
print("Languages are --> ", dic_courses["languages"])
print("First Language is --> ", dic_courses["languages"][0])
print("Second Language is --> ", dic_courses["languages"][1])