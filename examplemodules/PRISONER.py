from numpy import random

team_name = 'Ethan and Oliver'
strategy_name = 'Ethan and Olivers CRAAZY STRATEGY!!!!'
strategy_description = 'A secret strargegy'


def move(my_history, their_history, my_score, their_score, opponent_name):
    if their_history[-1:] == 'b':
        return 'b'
    elif their_history == 6:
        return 'b'
    else:
        return 'c'