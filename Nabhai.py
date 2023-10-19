def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y
def power(x, y):
    return x ** y
def floor_divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x // y
while True:
    print("""Options:
    	Enter 1 for addition
    	Enter 2 for subtraction
    	Enter 3 for multiplication
        Enter 4 for division
        Enter 5 for exponentiation
        Enter 6 for floor division
        Enter 'quit' to end the program"""
    c = input("enter your choice: ")
    if c == "quit":
        break
    elif c in ("add", "subtract", "multiply", "divide", "power", "floor"):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if c == "add":
            print("Result:", add(num1, num2))
        elif c == "subtract":
            print("Result:", subtract(num1, num2))
        elif c == "multiply":
            print("Result:", multiply(num1, num2))
        elif c == "divide":
            print("Result:", divide(num1, num2))
        elif c == "power":
            print("Result:", power(num1, num2))
        elif c == "floor":
            print("Result:", floor_divide(num1, num2))
    else:
        print("Invalid input")
