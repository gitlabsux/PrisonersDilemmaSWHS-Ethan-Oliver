
team_name = 'Ethan and Oliver'
strategy_name = 'Stupod Stragegy'
strategy_description = 'DUMB'


def move(my_history, their_history, my_score, their_score, opponent_name):
    if their_score > my_score:
        return 'b'
    elif their_score == my_score:
        return 'c'
    else:
        return 'c'
