## We have a simple game for 2 players. We have unkown number of matches on the table.
##One by one players chose 1, 2 or 3 matches. If you take more you break the rule and atomatically stop the game.
##if one of the players pulls the last match it means that he loses.

import random
print('We have a simple game for 2 players. We have unkown number of matches on the table.\n '
      'One by one our players chose 1, 2 or 3 matches.\nIf you take more, you break the rule and atomatically stop the game'
        'if one of the players pulls the last match it means that he loses.\n')
total = random.randint(10,15) # I decided to use random function because if I don`t want to know the number of matches,
                            # and every time it changes:
amount = total
# print(amount) - add it as a comment because it has to be unpredictable. But you can make as a function just to check
# how it works
choice = (int(input('Please chose your match....')))
while choice > 3:
    print('What are you doing??? I told you what to do.\nYou cann`t chose more than 3 matches.'
          ' You won`t play any more!!!!')
    break

rest = amount - choice
rest > 1
while choice <= 3:
    if rest > 1:
        choice = (int(input('Please chose your match....')))
        rest -= choice
    if rest > 1:
        continue
    if rest <= 1:
        break
    if choice > 3: # if after the first time you choose 1-3 matches but later decided more - you lose!!!
        break
print('Game Over. Thanks for your time')
### моє прохання до вас, чи не могли би ви підсказати мені як написати код так,
# щоби після того як я витяну 4 спічки за першим разом, мені появився коментарь що ти ламаєщ правила,
# але одночасно гру можна було розпочати заново а не закінчити автоматично як в мене