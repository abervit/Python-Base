# Working with strings
"""Creating a string"""
print("Giraffe Academy")
print("Giraffe \nAcademy")
print("Giraffe \"Academy") # allowing us to have a quotation mark before academy

"""Concatenation"""
phrase = "Giraffe Academy"
new_pharase = "Welcome to " + phrase
print(new_pharase) # --> Welcome to Giraffe Academy

"""Functions"""
phrase = "Giraffe Academy"
print(phrase.isalnum()) # --> False

print(phrase.lower()) # --> giraffe academy
print(phrase.upper()) # --> GIRAFFE ACADEMY
print(phrase.capitalize()) # --> Giraffe academy
print(phrase.swapcase()) # --> gIRAFFE aCADEMY
print(phrase.upper().isupper()) # --> True

print(len(phrase)) # --> 15
print(phrase.replace("Giraffe", "Crocodile")) # --> Crocodile Academy
print(phrase[2:5]) # --> raf

"""Index function tells where is the first occurrence of specified character. 
We also can specify the position space - like between 0th and 10th index of the string"""
print(phrase.index("a", 0, 15)) # --> 3
print(phrase.index("a")) # --> 3


