# Nested loops are a loop within a loop, an inner loop within the body of an outer one.
# Can use nested loops for working with two dimensions such as printing stars in rows and columns 

# When a print statement is executed, it prints the contents on a different line (\n)
# By using end = ""(using dash or space inside quotes), this prints everything on the same line

for x in range(3):
    for y in range(1, 10):
        print(y, end="")

print()


# Print a rectangle
rows = int(input("Enter the number of rows: "))
columns = int (input("Enter the number of columns: "))
symbol = input("Enter a symbol to use: ")


# Think of the outer loop as the rows
for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()