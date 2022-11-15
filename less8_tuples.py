# Tuples - a container (data structure) where we can store different values

"""Tuple creation. Tuple is immutable, can't be changed or modified"""
coordinates = (4, 5)
print(coordinates)  # --> (4, 5)
print(coordinates[0])  # --> 4

"""The difference between tuples and lists - immutability. Usually use for data that doesn't change"""
coordinates[0] = 23
print(coordinates)  # --> 'tuple' object does not support item assignment
