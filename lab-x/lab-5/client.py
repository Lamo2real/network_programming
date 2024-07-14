# client.py



import socket
from common import get_move, determine_winner, update_score, print_scores

def client(server_ip):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, 60003))

    score_server = 0
    score_client = 0

    while score_server < 10 and score_client < 10:
        move = get_move()
        client_socket.sendall(move.encode())
        opponent_move = client_socket.recv(1024).decode()
        print(f"Opponent's move: {opponent_move}")

        result = determine_winner(move, opponent_move)
        score_server, score_client = update_score(result, score_server, score_client)
        print_scores(score_server, score_client)

    if score_client == 10:
        print(f"You won with {score_client} against {score_server}")
        print(client_socket.recv(1024).decode())  #Receive the servers final message with the score presented in the print above
    else:
        print(f"You lost with {score_client} against {score_server}")
        print(client_socket.recv(1024).decode())  #Receive the servers final message with the score presented in the print above 

    client_socket.close()

if __name__ == "__main__":
    server_ip = input("Enter the server's IP address: ")
    client(server_ip)
