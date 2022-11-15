# For loop - allows us to loop through different type of collections

for i in range(5):
    print(i)

friends = ["Jim", "Karen", "Kevin"]
for i in friends:
    print(i)
for i in range(len(friends)):
    print(i)

for i in "letter":
    print(i)

for i in range(5):
    if i == 0:
        print("The first iteration")
    else:
        print("Not first")