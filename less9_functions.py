# Functions - a collection of code which performs a specific task
# Functions help us to organize our code better. Break up it in a little chunks that are doing different things

def say_hi():
    name = input("Enter your name: ")
    print(f"Hi, my dear {name}")


say_hi()  # --> Enter your name: Kev ==> Hi, my dear Kev

"""Passing perimeters to a function. Peace of information that we pass"""


def greet(name, age, city):
    print(f"Hello dear {name}. You are {age} years old, and live in {city}.")


greet("Tom", 24, "New York")  # --> Hello dear Tom. You are 24 years old, and live in New York.
greet("Olef", 43, "Boston")  # --> Hello dear Olef. You are 43 years old, and live in Boston.
