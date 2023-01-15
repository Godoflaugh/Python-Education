capitals = {"USA": "Washington D.C.", 
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

print(capitals.get("USA"))

dog = {"Name": "Rufus",
       "Breed": "Blue Staffy",
       "Legs": 4,
       "Age": 2}

student = {'first_name': 'Kevin',
           'last_name': 'Lam',
           'gender': 'male',
           'age': 31,
           'marital_status': 'single',
           'skills': ["tennis", 'cooking'],
           'country': 'USA',
           'city': 'Tustin',
           'address': '123 Fake St'}

print(len(student))
print(student["skills"][0])
print(type(student["skills"]))

student["skills"].append("html")
print(student["skills"])

#Get the dictionary Key's as a list
keys = student.keys()
print(keys)

#Get the dictionary's values as a list
values = student.values()
print(values)

#change the dictionary to a list of tuples
print(student.items())


#removing an item from the dictionary
student.pop("first_name")
print(student)

#clearing a dictionary
print(student.clear())

#deleting a dictionary
del student
