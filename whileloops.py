"""While loops  is used to repeatedly execute a block of 
code as long as a certain condition is true."""

"""Example: while condition:
    - code to be executed while the condition is true
    - this code will repeat until the condition becomes false
"""

# Rules when using a 'While loop'
"""Initialization of variables: Make sure to initialize any variables 
used in the loop before the loop starts.

Update the condition: Ensure that the loop's condition is updated 
inside the loop so that it will eventually become false and the loop will terminate.

Avoid infinite loops: Be cautious not to create infinite loops by making 
sure that the loop condition will eventually evaluate to false."""

# Print numbers from 1 to 10 using a while loop
# First we have to initiate a variable (where we want the count to start at)
num = 1
# Start the 'while' condition and include the number you want it to end at (include num)
while num <= 10:
    # Print out the variable
    print(num)
    # Now we need to increment by one each iteration
    num += 1


# print the square of numbers from 1 to 5 using a while loop
# Initialize a variable (where we want to begin the count)
counter = 1
# While condition began
# Continue looping while counter is less than or equal to 5
while counter <= 5:
    # Calculate the square of the current counter value
    square = counter ** 2
    # Print the result
    print(square)
    # Increment the counter by 1 in each iteration
    counter += 1



    
