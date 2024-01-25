# Declare a variable called myName & assign to it a string that represents your full name
myName = "Josette Nelson-Magruder"

# Declare a variable, tittled message and assign "Hello World" to the variable; print message
message = "Hello World"
print(message)

# Take input of students biodata in variables and print the input data
# Student Bio Data:
name = "Aisha Batool"
age = "17"
university_name = "Habib University"
course_name = "Computational Thinking-1"

print("\nStudent Bio Data: ")
print(f"{name}")
print(f"{age}")
print(f"{university_name}")
print(f"{course_name}")

""" Print the following by using one variable name only:
"PIZZA"
PIZZA
PIZZ
PIZ
PI
P """

food = "PIZZA"

# Print desired patterns through slicing
print(food)
print(food[:-1])
print(food[:-2])
print(food[:-3])
print(food[:-4])

""" Why pay a fortuneteller when you can just program your fortune yourself?
Store the following into variables: name, number of children, partner's name, geographia location, and job title
print your fortune like: you will be a Data Engineer in USA, and married with ABC kids"""

number_of_children = "4"
husband_name = "Kahlif Magruder"
geographic_location = "outside the US"
job_title = "Data Engineer"

print(f"In your future you will be a {job_title}, somewhere {geographic_location} married to {husband_name} with {number_of_children} kids.")

""" Declare a variable called email & assign to it a string that represents your Email
Address. Print the below mentioned message. (Hint use string concatenation) """

email = "joey123@noneya.com"

print(f"My email address is: {email}")


""" Declare a variable called book and give it value "Think Python". Print the following message:
"""
book = "Think Python"

print(f"I am trying to learn from the book {book}")

""" Use the variables, declared in Q3 and show the details giving meaning to data.
Student Bio Data
Please enter name:  Aisha Batool
Please enter age : 17
Please enter university name :  Habib University
Please enter course name: Computational Thinking-1"""

print(f"My name is {name}")
print(f"I am {age} years old")
print(f"I study in {university_name}")
print(f"I am enrolled in {course_name}")
