# Lists - a container which stores different type of information inside

friends = ["Kevin", "Karen", "Jim"]
print(friends.__len__())  # --> 3

"""Referring to elements by its index"""
print(friends[2])  # --> Jim
print(friends[-1])  # --> Jim
print(friends[1:]) # --> ['Karen', 'Jim']

friends.extend(["Oscar", "Toby"])
print(friends)

"""Modifying a single element or bunch of a array"""
friends = ["Kevin", "Karen", "Jim"]
friends[0] = "Andrew"
print(friends)

friends[1:] = ["June", "Leighton"]
print(friends)

