# Lists - a container which stores different type of information inside

friends = ["Kevin", "Karen", "Jim"]
print(friends.__len__())  # --> 3

"""Referring to elements by its index"""
print(friends[2])  # --> Jim
print(friends[-1])  # --> Jim
print(friends[1:])  # --> ['Karen', 'Jim']

friends.extend(["Oscar", "Toby"])
print(friends)  # --> ['Kevin', 'Karen', 'Jim', 'Oscar', 'Toby']

"""Modifying a single element or bunch of a array"""
friends = ["Kevin", "Karen", "Jim"]
friends[0] = "Andrew"
print(friends)  # --> ['Andrew', 'Karen', 'Jim']

friends[1:] = ["June", "Leighton"]
print(friends)  # --> ['Andrew', 'June', 'Leighton']

# List Functions

lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

"""Extend function - take a list and append it with other data"""
friends.extend(lucky_numbers)
print(friends)  # --> ['Kevin', 'Karen', 'Jim', 'Oscar', 'Toby', 4, 8, 15, 16, 23, 42]

"""Append a single element onto the end of the list"""
friends.append("Creed")
print(friends)  # --> ['Kevin', 'Karen', 'Jim', 'Oscar', 'Toby', 4, 8, 15, 16, 23, 42, 'Creed']

"""Insert - takes 2 perimeters: first position, second element"""
friends.insert(1, "Kelly")
print(friends)  # --> ['Kevin', 'Kelly', 'Karen', 'Jim', 'Oscar', 'Toby', 4, 8, 15, 16, 23, 42, 'Creed']

"""Removing elements"""
friends.remove(4)
print(friends)  # --> ['Kevin', 'Kelly', 'Karen', 'Jim', 'Oscar', 'Toby', 8, 15, 16, 23, 42, 'Creed']

# friends.clear() # --> clears a whole list by making it empty

print(friends.pop())  # --> Creed - removes the last item from the list and returns it
print(friends)  # --> ['Kevin', 'Kelly', 'Karen', 'Jim', 'Oscar', 'Toby', 8, 15, 16, 23, 42]

"""Checking if certain element is in the list"""
print(friends.index("Kevin"))  # --> 0 - index of this element

print(friends.count(16))  # --> 1

"""Sorting our list"""
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.sort()
print(friends)  # --> ['Jim', 'Karen', 'Kevin', 'Oscar', 'Toby']

friends.sort(reverse=-1)
print(friends)  # --> ['Toby', 'Oscar', 'Kevin', 'Karen', 'Jim']
friends.reverse()
print(friends)  # --> ['Jim', 'Karen', 'Kevin', 'Oscar', 'Toby']

"""Creating a copy of our list"""

friends1 = friends.copy()
print(friends1)  # --> ['Jim', 'Karen', 'Kevin', 'Oscar', 'Toby']
print(friends)  # --> ['Jim', 'Karen', 'Kevin', 'Oscar', 'Toby']
friends.append("Mark")
print(friends)  # --> ['Jim', 'Karen', 'Kevin', 'Oscar', 'Toby', 'Mark']
print(friends1)  # --> ['Jim', 'Karen', 'Kevin', 'Oscar', 'Toby']
