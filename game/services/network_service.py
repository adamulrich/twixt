import socket
import threading
from constants import *
from game.casting.point import Point

class NetworkService:

    game_over = False

    def __init__(self, host, port, client_server) -> None:

        if client_server == NETWORK_SERVER:
            self.host_game(host, port)
        else:
            self.connect_to_game(host, port)
            
        self.client = None

    
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((host, port))
        server.listen(1)

        self.client, self.addr = server.accept()


    def connect_to_game(self, host, port):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((host, port))

        #threading.Thread(target=self.handle_connection, args=(client,)).start()

    def get_data(self): 
        while True:
            data = self.client.recv(1024)
            position = data.decode('utf-8')
            print(position)
            return Point(position[0], position[1])


    def send_data(self, position: Point):
        self.client.send((position.get_x(), position.get_y()))


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




    