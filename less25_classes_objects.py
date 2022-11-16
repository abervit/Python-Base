# Classes &  Objects
# With classes we can create our own data type

class Student:
    """init is defining what is object of the class"""

    def __init__(self, name, major, gpa, is_on_probation):
        # self.name means -> student's name will be equal to a name that we pass,
        # the same with major, gpa and is_on_probation
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    """The object  is the instance of the class"""


"""if we want to import class Student from other file"""
""" from Student import Student """
student1 = Student("Mark", "Art", 3.2, False)
print(student1.name)  # --> Mark
