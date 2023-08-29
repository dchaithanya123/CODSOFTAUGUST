def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

print("Simple Calculator")
print("Operations:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

try:
    operation = int(input("Select operation (1/2/3/4): "))
    if operation in [1, 2, 3, 4]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if operation == 1:
            print("Result:", add(num1, num2))
        elif operation == 2:
            print("Result:", subtract(num1, num2))
        elif operation == 3:
            print("Result:", multiply(num1, num2))
        elif operation == 4:
            print("Result:", divide(num1, num2))
    else:
        print("Invalid operation choice.")
except ValueError:
    print("Invalid input. Please enter valid numbers and operation choice.")