# If statement - special structure in python to help the program make decisions
# We can execute a some code when certain conditions are true or other codes when not
# With if statement the program response to our input

is_male = False
is_tall = True

if is_male:
    print("Yes, he is male")
else:
    print("No, she is female")  # --> No, she is female

is_male = True
is_tall = True

if is_male or is_tall:
    print("Yes, he is male or tall, or both")  # --> Yes, he is male or tall, or both

else:
    print("No,he is neither male or tall or both")

is_male = False
is_tall = True

if is_male and is_tall:
    print("Yes, he is male or tall, or both")

else:
    print("No,he is neither male or tall or both")  # --> No,he is neither male or tall or both

is_male = False
is_tall = False

if is_male and is_tall:
    print("Yes, he is male or tall, or both")
elif is_male and not is_tall:
    print("He is male, but not tall")
elif not is_male and is_tall:
    print("He is not male but tall")
else:
    print("He is not male and not tall")
