print("Welcome to My Calculator")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Choose operation: +, -, *, /")
operator = input("Enter operation: ")

if operator == "+":
    print("Result:", num1 + num2)
elif operator == "-":
    print("Result:", num1 - num2)
elif operator == "*":
    print("Result:", num1 * num2)
elif operator == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operation")

