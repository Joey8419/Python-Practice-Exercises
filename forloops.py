# For loops are used to iterate over items of a collection, such as a string
# Because a string is a sequence of characters; it looks like a collection
# Can use for loop to iterate over each character in a string

# In each iteration, this variable will hold one item
""" Example: for (loop variable) in 'Python':
                    print(loop variable)"""

""" Lets define a list using square brackets in a for loop
for (loop variable) in ['Joey', 'John', 'Josh']:
    print(loopvariable)"""

"""Can also loop over a list of numbers
for (loop variable) in [1, 2, 3, 4, 5]:
    print(loop variable)"""

# Each one of those when code is executed is on a different line

# If you don't want to type out a list of numbers one by one, thats when you can use the range function
"""Example: for (loop variable) in range():
                print(loop variable)
                
If you give the range(10), it's gonna start counting from 0 and stop at number 9. 10 is NOT included
Range is an onject in python that can be iterated over. In each iteration, this object will spit out a new number.
Range can also be used as a start, stop, step method with commas separating them.
"""

""" Write a list of items in the shopping cart. Use a for loop to calculate 
the total cost of all items in the shopping cart"""

prices = [10, 20, 30]
total_cost = 0


for numbers in prices:
    total_cost += numbers

print(f"Total: {total_cost}")


""" for loops = execute a block of code a fixed number of times. You can iterate 
over a range, string, sequence, etc."""

for x in range(1, 11): # I want to count to 10; start @ 1 and count to 10
    # Whatever code needs to be repeated a certain number of times, list underneath for loop
    print(x)
# When we escape the for loop print something
print("HAPPY NEW YEAR!")

# Lets count backwards; Can use the reversed function and enclose the range function within the reversed function
for count in reversed(range(1, 11)):
    print(count)

print("HAPPY NEW YEAR")

# Now lets count from 1 -10 by 2's
for num in range(1, 11, 2):
    print(num)


# Iterate over a string
credit_card = "1234-5678-9012-3456"

for x in credit_card:
    # This prints each individual number separately on a new line
    print(x)


# Can use both "continue" and "break" in for/while loops
# Count to 20
for count in range(1, 21):
    # I want to skip over the number 13, use the 'continue' keyword 
    if count == 13:
        continue
    else:
        print(count)

# 'break' keyword just allows you to break out of the loop entirely
for x in range(1, 21):
    if x == 13:
        break # once 12 is reached it breaks the loops
    else:
        print(x)


# for loop in list
for i in [0, 1, 2]:
    print("meow")

# another way to do the for loop above
print("meow\n" * 3, end="")


"""Write a program to display the message "Hello World" 5 times in your browser using a for loop"""

for x in range(5):
    print("Hello World")


"""Write a program to print numeric counting from 1 to 10"""
for x in range(1, 11):
    print(x)


"""Write a program to print multiplication table of any number using a for loop.
Table number and length should be taken as an input from user.
Enter a number to enter its multiplication table: 2
Enter length of multiplication table: 15
Multiplication table of 2
Length of 13

2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
2 * 5 = 10
2 * 6 = 12
2 * 7 = 14
2 * 8 = 16
2 * 9 = 18
2 * 10 = 20
2 * 11 = 22
2 * 12 = 24
2 * 13 = 26 """

# Get input from user 
num_input = int(input("Enter a number to enter its multiplication table: "))
table_length = int(input("Enter length of multiplication table: "))

# Display multiplication table
print(f"Multiplication table for {num_input} (up to {table_length} times:  )")

for i in range(1, table_length + 1):
    product = table_length * i
    print(f"{num_input} * {i} = {product}")



"""Generate the following series in your browser.
Counting: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15
Reverse counting: 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
Even: 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20
Odd: 1, 3, 5, 7, 9, 11, 13, 15, 17, 19
Series: 2k, 4k, 6k, 8k, 10k, 12k, 14k, 16k, 18k, 20k"""

print("Counting:", end=" ")
for i in range(1, 16):
    print(i, end=", ")
print()

print("Reverse counting:", end=" ")
for i in range(10, 0, -1):
    print(i, end=", ")
print()

print("Even:", end=" ")
for i in range(0, 21, 2):
    print(i, end=", ")
print()

print("Odd:", end=" ")
for i in range(1, 20,2):
    print(i, end=", ")
print()

print("Series:", end=" ")
for i in range(2, 21, 2):
    print(f"{i}k", end=", ")
print()


# Write a program to print multiples of 5 ranging from 1 to 100
for x in range(5, 101, 5):
    print(x)


"""Write a program to repeatedly print the value of the variable num which is input by user.
Value should be decreasing by 0.5 each time, as long as x Value remains positive."""

num = float(input("Enter in a number: "))

# To "Repeat" code, use while loop
# Repeatedly print the value of num decreasing by 0.5 as long as it's positive
while num > 0:
    print(f"Current value of num: {num}")
    num -= 0.5


"""Write a for loop that will iterate from 0 to 20. For each iteration, it will check if the 
current number is even or odd, and report to the screen (e.g. "2 is even")."""

for i in range(0, 21):
    if i % 2 == 0:
        print(f"{i} is Even")
    elif i % 2 != 0:
        print(f"{i} is Odd") 
print()



"""Write a program to calculate the product of the odd integers from 1 to 7. The 
product of the odd integers from 1 to 7 is 105."""





"""Write a program that will write out a wedge of stars. The user will enter the initial
 number of stars, and the program will write out lines of stars where each line has one 
 few star than the previous line
 
 Initial number of stars: 7
 
 *******
 ******
 *****
 ****
 ***
 **
 *
 """ 
# Prompt user to enter in the number of stars
initial_stars = int(input("Enter the initial number of stars: "))
# Iterate over a range of numbers, starting from initial_stars, decreasing by 1, and stopping when it reaches 0 (exclusive).
for i in range(initial_stars, 0, -1):
    print('* ' * i)


# Print numbers from 1 to 10 using a for loop
for num in range(1, 11):
    print(num)


# A 'while loop' is used to repeatedly execute a block of code as long as a certain condition is true. 

"""Example: while condition:
     - code to be executed while the condition is true
     - this code will repeat until the condition becomes false"""

# Print numbers from 1 to 10 usig a while loop
num = 1 # This is the number we are starting the counting at
while num <= 10: # We want this number to be included in the count so it must be less than this number and equal to
    print(num)
    num += 1 # This is incrementing the number by 1 each iteration


# Print the square of numbers from 1 to 5 using a for loop
for num in range(1, 6):
    print(num **2)


# Print even numers from 2 to 20 using a for loop
for num in range(2, 21, 2):
    print(f"This numbers are even: {num}")


# Calculate the sum of numbers from 1 to 50 using a for loop
# Initialize the sum to 0
sum = 0
# Loop through numbers from 1 to 50 (inclusive)
for num in range(1, 51):
    # Add the current number to the sum
    sum += num
    # Print the final result
    print(sum)

# Print the factorial of a given number using a for loop
# Define the function of given number
def factorial(num):
    # Initialize the factorial number to 1
    factorial_num = 1

    # Loop through numbers from 1 to the given number (inclusive)
    for x in range(1, num + 1):
        # Multiply the current result by the current number
        factorial_num *= x 

    return factorial_num

# Print the elements of a list using a for loop
# Create a list that contains elements
lis = ["apple", "banana", "cucumber", "pineapple", "strawberry"]
# Loop through each element in the list
for name in lis:
    print(name)


# Print the length of each word in a sentence using a for loop
# Initialize the variable
sentence = "Hello, my name is Joey"
# Split the sentence into words using the split() method
words = sentence.split()
# Loop through each word in the list of words
for letters in words:
    # Print the length of the words in the sentence
    print(len(letters))


# Print the reverse of a string using a for loop
string = "This is the day that the lord has made"
# Initialize an empty string to store the reversed result
rev_sentence = ""
# Iterate through the characters of the original string in reverse order
for sentence in reversed(string):
    rev_sentence += sentence
    
print(rev_sentence)


# Print the Fibonacci sequence up to the 10th term using a for loop.
# Define a function
def print_fibonacci_sequence(terms):
    # Initialize the sequence with the first two terms
    fibonacci_seq = [0, 1]
    
    # Start the loop from the third term up to the specified number of terms
    for _ in range(0, terms):
        next_term = fibonacci_seq[-1] + fibonacci_seq[-2]
        fibonacci_seq.append(next_term)

    # Print the fibonacci sequence
    print("Fibonacci sequence up to the", terms, "terms:")
    print(fibonacci_seq)


# Calculate the average of a list of numbers using a for loop
lis = [1, 2, 3, 4, 5]
# Initialize sum to zero
sum_num = 0
# Loop through each number in the list
for num in lis:
    sum_num += num
    
# Calculate the average outside of loop
average = sum_num / len(lis)
print(average)


# Print a pattern of stars in a right-angled triangle using a for loop.
rows = int(input("Enter in the number of rows: "))
symbol = input("Enter in the symbol: ")


for i in range(1, rows + 1):
    print(symbol * i)
