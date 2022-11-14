# We have a game which is called "Matches". In this version of game it can be used for any amount of players and matches.
#But we want to play it with two random people. So here is why we ask about the number of players.


players = int(input("please enter number of players: \n"))
matches = int(input("please enter number of matches: \n"))
turn = 0 #we start with a rutn 0, until the first player will chose his match or matches


def rtn_player():
    player = turn % players
    return player if player > 0 else players


def get_answer():
    val = 0
    try:
        val = int(input("player " + str(rtn_player()) + " please select from 1,2 or 3: \n"))
    except ValueError:
        print("Not a number!")
    return val


while matches > 0:
    turn += 1 #a new turn for next player, until we have some matches left
    print("there are " + str(matches) + " matches remaining.\n")
    answer = 0
    while answer < 1 or answer > 3:
        answer = get_answer()
    matches -= answer


print("player " + str(rtn_player()) + " is the loser!")