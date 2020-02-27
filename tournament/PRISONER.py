import random

team_name = 'Ethan and Oliver'
strategy_name = 'Ethan and Olivers CRAAZY STRATEGY!!!!'
strategy_description = 'A secret strargegy'


def move(my_history, their_history, my_score, their_score):
    if 'b' in their_history[-5:]:  # If the other player has betrayed within last 5 rounds,
        return random.randint('b', 'c')  # RABNDOM
    if len(my_history) == 6:  # Always betray on round 7 LOL POGGERS
        return 'b'
    elif len(my_history) % 2 == 0 and len(my_history) < 39:  ## If it is an even round and it is not yet round 40
        if len(my_history) % 3 == 0:
            return 'b'
        else:
            return 'c'
    #    elif my_score < their_score:
    #        return "c"
    #    elif their_score < my_score:
    #        return "b"
    else:
        if their_history.count('b') > their_history.count('c'):
            return 'c'
        if their_history.count('b') < their_history.count('c'):
            return 'b'

