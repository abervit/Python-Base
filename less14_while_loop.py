# While loop - a structure in python which allows us to loop through
# an executed block of code multiple times

i = 1
while i <= 10:
    i += 1
    if i == 5:
        continue
    if i == 10:
        break
    print(i)
print("Done with a loop!")
