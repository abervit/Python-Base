# Working with numbers

print(2)  # --> 2
print(2.33)  # --> 2.33
print(-3.4)  # --> -3.4

print(3 * 4 + 5)  # --> 17
print(3 * (4 + 5))  # --> 27
print(10 % 3)  # --> 1 (means 10 divided by 3 is 3 with a remainder 1)
print(10 // 3)  # --> 3 (means 10 holds 3 times of whole 3 number)

"""Storing numbers inside variables"""
num = 1
print(num)  # --> 1

"""Converting a number into a 'string', tuple and 'set' """
num = 1
print(str(num))  # --> 1
# print(tuple(num)) # --> TypeError: 'int' object is not iterable
# print(set(num)) # --> TypeError: 'int' object is not iterable

""" Math functions """
num = -5
print(abs(num))  # --> 5 (absolute value of negative number)
print(pow(num, 4))  # --> 625
print(max(1, 0, 13, -4))  # --> 13
print(min(1, 0, 13, -4))  # --> -4

print(round(3.4))  # --> 3
print(round(3.9))  # --> 4

from math import *

print(floor(3.9))  # --> 3
print(ceil(3.1))  # --> 4
print(sqrt(36))  # --> 6.0 (returns the square root of a number)


class Number:
    instances = []

    def __init__(self, number):
        self.number = number

    def __repr__(self):
        return str(self.number)

    def __add__(self, other):
        return self.number + other.number


num1 = Number(33)
num2 = Number(-23.34)
print(num1)  # --> 33
print(num2)  # --> -23.34
print(type(num1))  # --> <class '__main__.Number'>
print(num1.__add__(num2))
