import socket
from threading import Thread

server = None
ip_address = "127.0.0.1"
port = 5000

CLIENT = {}

def acceptConnections():
    global server
    global CLIENT 
    
    while True:
        player_socket , addrs = server.accept()
        playerName = player_socket.decode().strip()
        print(playerName)

        if(len(CLIENT.keys) == 0):
            CLIENT[playerName] = {"player_type" : "player1"}
        else:
            CLIENT[playerName] = {"player_type": "player2"}
        
        CLIENT[playerName]["player_socket"] = player_socket
        CLIENT[playerName]["address"] = addrs
        CLIENT


def setup():
    print("\t\t\t\t\t\t*** WELCOME TO TAMBOLA GAME ***")

    global server
    global port
    global ip_address

    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind(ip_address,port)
    server.listen(10)

    print("\t\t\t\t\t\t*** SERVER AWAITING CONNECTION ***")
