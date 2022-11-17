asked_questions = [
    "What`s your name?\n(1) Mark \n(2) Tom \n(3) John\n",
    "How old are you?\n(1) 6 y.o. \n(2) 23 y.o. \n(3) 2302 y.o.\n",
    "Where do you live?\n(1) Warsaw \n(2) Aberystwyth \n(3) Vancouver\n"
]

"""Creating class Question to keep our questions and answers"""


class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


"""Creating a new array - creating question objects - with question and its answer"""
"""each question (i) in questions is a new object of class Question"""
questions = [
    Question(asked_questions[0], "1"),
    Question(asked_questions[1], "2"),
    Question(asked_questions[2], "3")
]
for i in questions:
    print(i.prompt, i.answer)

"""Creating a function which has 1 perimeter - questions"""


def game(questions):
    score = 0  # to track how many correct answers we have
    for i in questions:
        answer = input(i.prompt)  # to ask a question our user
        if answer == i.answer:  # check if the answer is correct
            score += 1
    print(f"The game is over. You have {score}/" + str(len(questions)) + " points!!!")
    print("The game is over. You have " + str(score) + "/3 points!!!")


game(questions)
