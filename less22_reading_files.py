# Reading files

"""First we write the name of the file, next we specify the mode we want to use this file"""
open("employees.txt", "r")  # --> "r" - means for reading, not for modifying or changing
open("employees.txt", "w")  # --> "w" - means we can change it and modify
open("employees.txt", "a")  # --> "a" - means append information but can't change it or modify
open("employees.txt", "r+")  # --> "r+" - means read and write at the same time

"""Storing a file inside a variable"""
employee_file = open("example.txt", "r")

"""Checking if we can read file - if it's readable"""
print(employee_file.readable())  # --> True

"""Spit out all the information inside the file"""
print(employee_file.read())

"""Reading individual lines of the file"""
print(employee_file.readlines())  # --> reading the first line
"""We have always be sure we close the file after we use it"""
employee_file.close()

employee_file = open("example.txt", "r")
print(employee_file.readable())  # --> True
print(employee_file.readline())  # --> reading the first line
employee_file.close()

employee_file = open("example.txt", "r")
print(employee_file.readable())  # --> True
print(employee_file.readlines())  # --> reading all lines
employee_file.close()

"""if we want to access a specific line we use indexing"""
employee_file = open("example.txt", "r")
print(employee_file.readable())  # --> True
print(employee_file.readlines()[2])  # --> Mark - C
employee_file.close()

"""Using a for loop for reading a file"""
employee_file = open("example.txt", "r")
print(employee_file.readable())  # --> True
for i in employee_file.readlines():
    print(i)  # --> prints out all the lines
employee_file.close()

file = open("/Users/Witoldo/Desktop/Test Job.txt", "r")
print(file.readable())  # --> True
print(file.read())
file.close()
