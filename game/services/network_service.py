import socket
import threading
from constants import *
from game.casting.point import Point

class NetworkService:

    game_over = False

    def __init__(self, host, port, client_server) -> None:
        
        self.client = None

        if client_server == NETWORK_SERVER:
            self.host_game(host, port)
        else:
            self.connect_to_game(host, port)
            

    def host_game(self, host, port):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        server.bind((host, port))
        server.listen(1)

        self.client, self.addr = server.accept()
        self.client.setblocking(0)


    def connect_to_game(self, host, port):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host, port))
        self.client.setblocking(0)

    def get_data(self): 
        try:
            data = self.client.recv(2048)
            x, y = [int(i) for i in data.decode('utf-8').split('\n')]
            p: Point = Point(x,y)
            return p

        except:
            return None

    def send_data(self, position: Point):
         x = position.get_x()
         y = position.get_y()
         self.client.sendall(str.encode("\n".join([str(x), str(y)])))


