# Try except
"""Catching errors in python"""

try:
    number = int(input("Enter a number: "))
    print(number)
except:  # too broad, we have to catch specific errors not all of them at once
    print("Invalid input")

try:
    value = 10 / 0
except ZeroDivisionError as zero:  # storing the error as a variable
    print(zero)

try:
    value = 10 / 0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError:
    print("Divided by zero")
except ValueError:
    print("Invalid input")
