""" Write a prpogram that takes two nubers and adds them in a new variable. print
the result"""

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

result = num1 + num2

print(result)


""" Repeat Q1 for subtraction, multiplication, division, and modulus """

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

result1 = num1 + num2
result2 = num1 - num2
result3 = num1 * num2
result4 = num1 / num2
result5 = num1 % num2

print(result1)
print(result2)
print(result3)
print(result4)
print(result5)

""" Do the following using Mathematic Expressions
a) Declare a variable and initialize the variable with some number
b) Show the value of variable in your browser like "Initial value: 3"
c) Add 7 to the variable
d) Show value of variable in browser like "Value after addition is: 10"
e) Show the remainder after dividing the variables value by 3. Output "The remainder is: 1"

Initial value: 3
value after addition: 10
The remainder: 1
"""

# a) Declaring and initializing the variable
var_num = 3
# b) Show initial value in browser
print({var_num})
# c) Add 7 to the variable
var_num += 7
# d) Show value after addition
print({var_num})
# e) Show remainder after dividing the variables value by 3
remainder = var_num % 3
print({remainder})

""" Cost of one movie ticket is 600 PKR. Store ticket price in a variable and calculate
the cost of buying 5 tickets to a movie. Total cost to buy 5 tickets to a movie is 3000 PKR"""

movie_ticket = 600

result = 5 * movie_ticket

print(result)

""" Take a number input from user and print it's multiplication table. (Without using
any loops). """

num_input = int(input("Enter a number: "))

print(f"{num_input} * 1 = {num_input} * 1")
print(f"{num_input} * 2 = {num_input} * 2")
print(f"{num_input} * 3 = {num_input} * 3")
print(f"{num_input} * 4 = {num_input} * 4")
print(f"{num_input} * 5 = {num_input} * 5")
print(f"{num_input} * 6 = {num_input} * 6")
print(f"{num_input} * 7 = {num_input} * 7")
print(f"{num_input} * 8 = {num_input} * 8")
print(f"{num_input} * 9 = {num_input} * 9")
print(f"{num_input} * 10 = {num_input} * 10")
print(f"{num_input} * 11 = {num_input} * 11")
print(f"{num_input} * 12 = {num_input} * 12")

"""The Temperature Converter: It's hot out! Let's make a converter based on the steps here
 a) Store a Celsius temperature into a variable
 b) Convert it to Fahrenheit & output "NNC is NNF"
 c) Now store a Fahrenheit temperature into a variable
 d) Convert it to Celsius and output "NNF is NNC"
 """

# a) Store C temp into a variable
C_temp = 18
# b) Convert C to F
fahrenheit_temp = (C_temp * 9/5) + 32
# c) Store F temp into variable
F_temp = 75
# d) Convert F to C
Celsius_temp = (F_temp - 32) * 5/9

print(f"{C_temp} is {fahrenheit_temp}")
print(f"{F_temp} is {Celsius_temp}")
