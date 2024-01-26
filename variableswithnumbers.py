# Declare a variable called age & assign to it your age. Print your age
age = 33
print(age)

""" Declare and initialize a variable to keep track of how many times a visitor has visited 
your program. Show his/her number of visits on your program. For example: you have
visited this site N times"""

visits = 5

print(f"You have visited this site {visits} {'time' if visits == 1 else 'times'}.")



""" Declare a variable called birth year and assign to it your birth year. Also print
they type of your variable using type(). Print the following message: My birth year is 1990
Data Type of my declared variable is <class 'int'>"""

birth_year = 1990
print(type(1990))
print(f"My birth year is {birth_year}")
print(f"Data type of my declared variable is {type(1990)}")

""" A visitor visits an online clothing store www.xyzClothing.com. Write a python
script to store in variables the following information: 
a) Visitor's name, b) Product title, c) Quantity i.e how many products a visitor
wants to order. Show "John Doe ordered 5 T-shirt(s) on XYZ Clothing store" """

visitor_name = "John Doe"
product_title = "T-shirt"
quantity = 5

print(f"{visitor_name} ordered {quantity} {product_title}(s) on XYZ Clothing store")

""" Write a program that obtains four integer values from the user and displays the sum
and the product."""

first_num = 2
sec_num = 5
third_num = 7
fourth_num = 9

Sum_of_num = first_num + sec_num + third_num + fourth_num
product_of_num = first_num * sec_num * third_num * fourth_num

print(Sum_of_num)
print(product_of_num)


""" Write a program that obtains four float values from the user and displays the sum
and the product"""

num1 = 2.0
num2 = 5.0
num3 = 7.0
num4 = 9.0

sum_num = num1 + num2 + num3+ num4

print(sum_num)