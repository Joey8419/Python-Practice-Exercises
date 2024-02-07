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


""" for loops = execute a bloack of code a fixed number of times. You can iterate 
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


# Nested For loops
# Nested for loops are multiple for loops inside of each other


