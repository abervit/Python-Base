# Building a basic calculator

"""By default, python is taking a string as an answer, so we have to convert the number into int or float"""
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

result = num1 + num2
print(result)

# Building a better calculator

num1 = float(input("Enter first number: "))
operator = input("Enter your operator: ")
num2 = float(input("Enter second number: "))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
else:
    print("Invalid operator")
