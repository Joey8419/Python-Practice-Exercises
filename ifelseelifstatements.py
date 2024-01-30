""" Write a program to check whether the given input number is divisible by 3 or else show a message 
"Number is not divisible by 3."""

given_input = int(input("Enter a number: "))

if given_input % 3 == 0:
    print("This number is divisible by 3")
else:
    print("This number is NOT divisible by 3")


""" Write a program that checks whether the given input is an even number or an odd number"""

num_input = int(input("Enter a number: "))

if num_input % 2 == 0:
    print("This number is even")
else:
    print("This number is odd")


""" Write an if/else statement with the following condition: If the variable age is greater
than 18, output "Old enough", otherwise output "Too young"."""

age = int(input("How old are you? "))

if age > 18:
    print("Old enough")
else:
    print("Too young")


""" Write a program that prompts the user for their name, and then displays a special greeting to 
that person if their name is the same as yours. If the name entered by the user is anything
other than your name, your code should not produce any output."""

my_name = "Josette Nelson-Magruder"

name_input = input("Please enter your name: ")

if name_input == my_name:
    print("This is Amazing! We have the same name")


""" Write a program that takes a calendar year in YYYY format in a variable. Check and 
notify the user whether it is a leap year or not."""

calendar_year = int(input("Enter a year in YYYY format: "))

if (calendar_year % 4 == 0 and calendar_year % 100 != 0) or (calendar_year % 400 == 0):
    print(f"{calendar_year} is a leap year.")
else:
    print(f"{calendar_year} is NOT a leap year.")


""" Write a JavaScript program that accepts two integers and display the larger. Also
show if the two integers are equal."""

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 > num2:
    print(f"The larger integer is {num1}")
elif num2 > num1:
    print(f" The larger integer is {num2}")
else:
    print("Both numbers are equal")


""" Write a program that takes input a number from user and state whether the number 
is positive, negative, or zero."""

num_input = int(input("Enter a number: "))

if num_input > 0:
    print("This number is positive.")
elif num_input < 0:
    print("This number is negative.")
else:
    print("This number is zero.")


""" Write a program that takes a character (i.e string of length 1) and returns true if
it is a vowel, false otherwise"""

character = input("Enter in a letter: ")

if len(character) == 1 and character.lower() in 'aeiou':
    print("True")
else:
    print("False")


""" Use a conditional (ternary) operator for this exercise:
If the variable age is a value below 18, the value of the variable is voteable should be 
"Too young", otherwise the value of voteable should be "Old enough"."""

age = int(input("Enter in your age: "))

# Using a ternary operator
voteable = "Old enough" if age >= 18 else "Too young"

print(voteable)
