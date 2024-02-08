# Dictionaries = data structure that has key value pairs and are mutable
# keys are unchangeable/ immutable; use curly brackets {}

students = {"Joey": "Second grade", "Josh": "Fifth grade", "John": "Third grade", "Sasha": "Fifth grade"}

# Get the value of the key in the dictionary by looking up the students name (key)
# Curly brackets now become square brackets
print(students["John"])
print(students["Joey"])
print(students["Josh"])
print(students["Sasha"])

# When using a for loop to iterate over a dictionary, it iterates over all the keys
for student in students:
    print(student)

# Print out both if you want keys and value pairs
for student in students:
    print(student, students[students], sep=", ") # Seperator is used here to make code more readable

# None represents the absence of a value
# LISTS OF DICTIONARIES
students = [{"name": "Joey", "grade": "Second grade", "subject": "Math"},
            {"name": "Josh", "grade": "Fifth grade", "subject": "History"}, 
            {"name": "John", "grade": "Third grade", "subject": "Reading"}, 
            {"name": "Sasha", "grade": "Fifth grade", "subject": "Art"}]

for student in students:
    print(student["name"], student["house"], student["subject"], sep=", " )

