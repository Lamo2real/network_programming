# common.py




def get_move():
    move = input("Your move (R, P, S): ").upper()
    while move not in ['R', 'P', 'S']:
        move = input("Invalid move. Enter R, P, or S: ").upper()
    return move

def determine_winner(move1, move2):
    if move1 == move2:
        return 0
    elif (move1 == 'R' and move2 == 'S') or (move1 == 'S' and move2 == 'P') or (move1 == 'P' and move2 == 'R'):
        return 1
    else:
        return -1

def update_score(result, score_server, score_client):
    if result == 1:
        score_server += 1
    elif result == -1:
        score_client += 1
    return score_server, score_client

def print_scores(score_server, score_client):
    print(f"Score: ({score_server}, {score_client})")
