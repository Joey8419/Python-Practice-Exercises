""" Write a program that takes inout a name from user and greet the user like this: 
Please enter your name: John Doe; Hi, John Doe"""

user_input = input("Please enter your name: ")
print(f"Hi, {user_input}")

""" Write a program to take "city" name as input from user. If user enters "Karachi" 
welcome the user like this: "Welcome to city of lights". Please Enter Your City: Karachi
Welcome to city lights"""

user_city = input("Please Enter Your City: ")

if user_city == "Karachi":
    print("Welcome to city of lights!")
else:
    print(f"Welcome to {user_city} !")