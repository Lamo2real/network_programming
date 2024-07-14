# server.py



import socket
from common import get_move, determine_winner, update_score, print_scores

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 60003))
    server_socket.listen(5)
    print("Waiting for connection...")
    conn, addr = server_socket.accept()
    print(f"Connected to {addr}")

    score_server = 0
    score_client = 0

    while score_server < 10 and score_client < 10:
        move = get_move()
        conn.sendall(move.encode())
        opponent_move = conn.recv(1024).decode()
        print(f"Opponent's move: {opponent_move}")

        result = determine_winner(move, opponent_move)
        score_server, score_client = update_score(result, score_server, score_client)
        print_scores(score_server, score_client)

    if score_server == 10:
        print(f"You won with {score_server} against {score_client}")
        conn.sendall(b'You lost')
    else:
        print(f"You lost with {score_server} against {score_client}")
        conn.sendall(b'You won')

    conn.close()

if __name__ == "__main__":
    server()
