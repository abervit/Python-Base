# Building a guessing game

secret_word = "giraffe"
guess = ""
limit = 3
guess_count = 0
out_of_guesses = False

while guess != secret_word and not out_of_guesses:
    if guess_count < limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("You lose!")
else:
    print("you win!")