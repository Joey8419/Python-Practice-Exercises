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