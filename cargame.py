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