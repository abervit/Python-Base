# Return Statement

"""When we want to get some information back from a function - we use 'return' statement"""


def cube(number):
    """after return statement we can't write a code, it won't work"""
    return number ** 3, number * number * number


cube(3)
print(cube(3))  # --> (27, 27)

result = cube(4)  # stores the value of cube(4)
print(result)  # --> (64, 64)
