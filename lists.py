# Lists = used to store multiple items in a single variable.
# Lists use square brackets []; they are mutable

students = ["Joey", "John", "Josh"]

# How do you print out each of these students (NOT ALL AT ONCE IN THE SAME LIST)
# How do you precisely print out which value you want from the list?
# You index into the list based on the position/ index of the value inside that list
print(students[0])
print(students[1])
print(students[2])

# As a FOR LOOP
students = ["Joey", "John", "Josh"]

for student in students:
    print(student)


# len() function = returns the number of items in an object
students = ["Joey", "John", "Josh"]

for i in range(len(students)):
    print(students[i])


# None represents the absence of a value
# LISTS OF DICTIONARIES
students = [{"name": "Joey", "grade": "Second grade", "subject": "Math"},
            {"name": "Josh", "grade": "Fifth grade", "subject": "History"}, 
            {"name": "John", "grade": "Third grade", "subject": "Reading"}, 
            {"name": "Sasha", "grade": "Fifth grade", "subject": "Art"}]

for student in students:
    print(student["name"], student["house"], student["subject"], sep=", " )
