x = 0
operation = ""
y = 0
valid_operations = ["+", "-", "*", "/", "^"]

x = input("Enter a number: ")
while x.isdigit() == False:
    print("Invalid Input, please input a number.")
    x = input("Enter a number: ")

print("Available Operations: " + ", ".join(valid_operations))
operation = input("Enter an operation: ")

while operation not in valid_operations:
    print("Invalid Operation, please input correct operation from list of available operations.")
    operation = input("Enter a valid operation: ")
    
if operation == "^":
    print("The squared result of", x, "is:", int(x) ** 2)
    exit()
    
y = input("Enter another number: ")
while y.isdigit() == False:
    print("Invalid Input, please input a number.")
    y = input("Enter another number: ")

if operation == "+":
    print("The addition", x, operation, y, "is:", int(x) + int(y))
elif operation == "/":
    print("The division", x, operation, y, "is:", int(x) / int(y))
elif operation == "-":
    print("The subtraction", x, operation, y, "is:", int(x) - int(y))
elif operation == "*":
    print("The multiplication", x, operation, y, "is:", int(x) * int(y))

