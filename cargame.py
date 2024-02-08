# While loop = execute some code WHILE some condition remains true
# Wile loop/ Conditional exercise

command = ""
started = False
stopped = False

# This block of code will be executed until the quit command is used and then the code 
# explicitly breaks out of the loop
while True:
    # To not repeat yourself in code, append the .lower() method so that every command will be in lowercase
    command = input("> ").lower()
    if command == "start":
         print("Car started...")
         if started:
              print("The car is already started!")
    elif command == "stop":
         print("Car stopped.")
         if stopped:
              print("The car is already stopped!")
    elif command == "help":
         # Here we want to print a multiline string
         print("""
    start - to start the car
    stop - to stop the car  
    quit - to quit
               """)
    elif command == "quit":
         break
    else:
         print("Sorry, I don't understand that! ")


i = 0
while i < 3:
     print("meow")
     i =+ 1


"""When you want to get user input that matches a certain expectation you have, you just
immediately say "while True". An infinite loop becomes induced (which goes on forever;
It will always be True."""

while True:
     n = int(input("What's n? "))
     if n < 0:
          continue
     else:
          break
     
# OR

# If user puts in a negative number it will continue to go through the while loop
while True:
     n = int(input("What's n? "))
     if n > 0:
          break

# When user inputs a positive number, this code block now gets executed     
for i in range(n):
     print("meow")


# Now create a function based on the the while loop above
def main():
     number = get_number
     meow(number)


def get_number():
     while True:
        n = int(input("What's n? "))
        if n > 0:
          return n


def meow(n):
     for _ in range(n):
          print("meow")


main()


name = input("Enter your name: ")

if name == "":
     print("You did not enter your name")
else:
     print(f"Hello {name}")


# Now rewrite the code above as a while loop
name = input("Enter your name: ")    
    
while name == "":
     print("You did not enter your name")
     # Without this line of code the while loop becomes an infinite loop; we give the user an EXIT stategy with this line of code
     name = input("Enter your name: ")

# Once user enters name, the while loop is exited and this is printed
print(f"Hello {name}")


age = int(input("Enter your age: "))

while age < 0:
     print("Age can't be a negative number")
     age = int(input("Enter your age: "))

print(f"you are {age} years old")


# Enter your favorite food
food = input("Enter your favorite food (q to quit): ")

while not food == "q":
     print(f"You like {food}")
     food = input("Enter your favorite food (q to quit): ")

print("Bye!")


# Using the OR operator
num = int(input("Enter a number between 1 -10: "))

while num < 1 or num > 10:
     print(f"{num} is not valid")
     num = int(input("Enter a number between 1 -10: "))

print(f"")
