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


"""Write a program to take "gender" as an input from user. If the user is male, give
the message: Good morning Sir. If the user is female, give the message: Good morning Ma'am"""

user_gender = input("Are you male or female? ")

if user_gender == "male":
    print("Good Morning Sir")
if user_gender == "female":
    print("Good Morning Ma'am")
else:
    print("Good Morning")


""" Write a program to take input max age and current age from user. If the current age
is less than or equal to max age, show the message "You are welcome". """

max_age = int(input("Enter the maximum age: "))
current_age = int(input("Enter your current age: "))

if current_age <= max_age:
    print("You are welcome")
else:
    print("Sorry you are not welcome")


"""Write a program to take input remaining fuel in car (in litres) from user. If the 
current fuel is less than 0.25litres, show the message "Please refill the fuel in your car". """

remaining_fuel = float(input("Enter the amount of fuel in litres left in your car: "))

if remaining_fuel < 0.25:
    print("Please refill the fuel in your car")
else:
    print("Check tank you might need gas soon")

   
    """ Write a program to take input the marks obtained in three subjects and total marks. 
    Compute and show the resulting percentage on your page. Take percentage and compute grade as per following table:
    Show the total marks, marks obtained, percentage, grade, and remarks like:
    Marks Sheet
    Total Marks: 300
    Marks Obtained: 219
    Percentage: 73%
    Grade: B
    Remarks: You need to improve"""

# Get input for marks obtained in three subjects and total marks
subject1_marks = int(input("Enter marks obtained in subject 1: "))
subject2_marks = int(input("Enter marks obtained in subject 2: "))
subject3_marks = int(input("Enter marks obtained in subject 3: ")) 
total_marks = int(input("Enter total marks: "))  

# Calculate total marks obtained
marks_obtained = subject1_marks + subject2_marks +subject3_marks

# Calculate the percentage
percentage = (marks_obtained / total_marks) * 100

# Determine grade based percentage
if percentage >= 80:
    grade = "A-one"
    remarks = "Excellent"
elif percentage >= 70:
    grade = "A"
    remarks = "Good"
elif percentage >= 60:
    grade = "B"
    remarks = "You need to improve"
else:
    grade = "Fail"
    remarks = "Sorry"

print("\nMarks Sheet")
print(f"Total Marks: {total_marks}")
print(f"Marks Obtained: {marks_obtained}")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")
print(f"Remarks: {remarks}")


"""Write a program to implement checkout process of a shopping cart system for an
e-commerce website. Take input from users, the following:
a) Name of item1
b) Name of item2
c) Price of item 1
d) Price of item 2
e) Ordered quantity of item 1
f) Ordered Quantity of item 2
g) Shipping charges
Compute the total cost. If the total cost is above 2000 PKR, offer them 10%
discount & show the receipt in your browser.
Shopping Cart
Price of T-Shirt is 1000
Quantity of T-Shirt is 2
Price of USB Flash Drive is 3
Shipping Charges 250
Total Cost of Your Order is 4350 PKR
Discounted Price is 3915 PKR"""

item1_name = input("Name of first item: ")
item2_name = input("Name of second item: ")
price1 = float(input("What is the price of the first item: "))
price2 = float(input("What is the price of the second item: "))
quantity1 = int(input("What is the quantity of the first item: "))
quantity2 = int(input("What is the quantity of the second item: "))
shipping_charges = float(input("Shipping charges: "))

total_cost = (price1 * quantity1) + (price2 * quantity2) + shipping_charges

if total_cost >= 2000:
    discount_percentage = 10
    discount_amount = (discount_percentage / 100) * total_cost
    discounted_price = total_cost - discount_amount

print("\nShopping Cart")
print(f"Price of {item1_name} is {price1} PKR")
print(f"Price of {item2_name} is {price2} PKR")
print(f"Quantity of {item1_name} is {quantity1}")
print(f"Quantity of {item2_name} is {quantity2}")
print(f"Shipping charges: {shipping_charges} PKR")
print(f"Total Cost Of Your Order is {total_cost} PKR    ")

# Display discounted price
if discounted_price != total_cost:
    print(f"Discounted Price is {discounted_price} PKR")


""" Store a secret number (ranging from 1 to 10) in a variable.
Prompt user to guess the secret number.
a) If user guesses the same number, show “Bingo! Correct answer”.
b) If the guessed number +1 is the secret number, show “Close enough to the
correct answer”."""

secret_num = 7
user_guess = int(input(" Enter a number from 1 to 10: "))

if user_guess == secret_num:
    print("Bingo! Correct answer")
elif user_guess + 1 == secret_num: 
    print("Close enough to the correct answer")
else:
    print("Wrong number. Guess again")


"""Write a program to check whether the given number is divisible by 3. Show the
message to the user if the number is divisible by 3."""

given_num = int(input("Enter given number: "))

if given_num % 3 == 0:
    print("This number is divsible by 3")
else:
    print("This number is NOT divisible by 3")


"""Write a program that checks whether the given input is an even number or an
odd number."""

num_input = int(input("Enter a number: "))

if num_input % 2 == 0:
    print("This is an even number")
else:
    print("This is an odd number")


""" Weather in Karachi nowadays is too cool, write a program that takes temperature
as input and shows a message based on following criteria:
a) T > 40 then “It is too hot outside.”
b) T > 30 then “The Weather today is Normal.”
c) T > 20 then “Today’s Weather is cool.”
d) T > 10 then “OMG! Today’s weather is so Cool.”"""