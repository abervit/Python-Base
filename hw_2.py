### When we want to calculate the area of the triangle using the Herons method, we must have all three sides of the
# our figure. Then we need to calculate the half of triangle perimeter after we can check our area.
print("Heron`s method of calculating triangle area")
side1 = float(input("Enter a length of the side 1: "))
side2 = float(input("Enter a length of the side 2: "))
side3 = float(input("Enter a length of the side 3: "))

s = (side1+side2+side3)/2
print(s)
area = (s*(s-side1)*(s-side2)*(s-side3))**0.5
print("The area of the triangle is", + area)
