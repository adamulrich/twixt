import socket
import threading
from constants import *

class NetworkService:

    game_over = False

    def __init__(self, host, port, client_server) -> None:

        if client_server == NETWORK_SERVER:
            self.host_game(host, port)
        else:
            self.connect_to_game(host, port)
            

    
    def host_game(self, host, port):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((host, port))
        server.listen(1)

        client, addr = server.accept()

        self.server = PLAYER_RED
        self.client = PLAYER_BLACK
        self.me = PLAYER_RED

        threading.Thread(target=self.handle_connection, args=(client,)).start()
        server.close()


    def connect_to_game(self, host, port):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((host, port))

        self.server = PLAYER_BLACK
        self.client = PLAYER_RED
        self.me = PLAYER_BLACK

        threading.Thread(target=self.handle_connection, args=(client,)).start()

    def handle_connection(self, client):
        while not self.game_over:
            if self.turn == self.you:
                # get mouse input
                pass

            else:
                data = client.recv(1024)
                if not data:
                    client.close()
                    break
                else:
                    #make move
                    move = data.decode('utf-8')




    