import constants
from game.casting.actor import Actor
from game.casting.pieces import Pieces
from game.casting.peg import Peg
from game.casting.point import Point
from game.services.network_service import NetworkService
from typing import List
import socket
import threading
from constants import *

class Player(Actor):
    """The responsibility of Player is to keep track of all the pegs and bridges that the player has and to determine 
        if a move is valid, or if the player has won.

    Args:
        Actor (_type_): super class
        _pieces: pieces that belong to the player
        _direction: the player 1 or 2
    """

    PORT = 9999
    IPADDRESS = "0.0.0.0"


    def __init__(self, color, direction):
        super().__init__(color=color, position=Point(0,0),text="")
        self.me = False
        self._pieces = Pieces()
        self._direction = direction
        self.client_server = NETWORK_NONE
        self.network_service = None
        self.current_turn = None

        if color==RED:
            self.color_name = "RED"
        else:
            self.color_name = "BLACK"


    def get_pegs(self):
        """returns the list of this players pegs from the pieces object
        """
        return self._pieces.get_peg_list()

    def get_peg_locations(self) -> list[Point]:
        """returns a list of only the peg locations as points
        """
        return_list = []
       
        for p in self._pieces.get_peg_list():
            pt = p.get_screen_position()
            return_list.append(pt)
        return return_list

    def get_bridges(self):
        """returns the list of this players current bridges 
        """
        return self._pieces.get_bridge_list()


    def add_peg(self, peg):
        """adds a peg to this players pieces object

        Args:
            peg (_type_): peg to add
        """
        self._pieces.add_peg(peg)

    def add_bridge(self, peg1, peg2):
        """adds a bridge to the pieces location

        Args:
            peg1: one end of the bridge
            peg2: other end of the bridge
        """
        self._pieces.add_bridge(peg1, peg2)

    def remove_bridge(self):
        pass

    def get_possible_bridge_endpoints_from_peg(self, peg: Peg):
        """ returns the possible bridge nodes based on current node 
            locations. iig i

        Args:
            peg (Peg): a peg location to evaluate

        """
        return_list = []
        #get all spots on the board that could be possible, up to 8
        possible_bridges = peg.get_possible_bridge_endpoints_on_board()
        peg_list = self.get_pegs()
        # walk the possible locations, and see if they match any current pegs
        for endpoint in possible_bridges:
            for current_peg in peg_list:
                if current_peg.get_position().get_x() == endpoint.get_position().get_x() \
                and current_peg.get_position().get_y() == endpoint.get_position().get_y():
                    return_list.append(current_peg)
        return return_list

    def get_possible_new_bridge_list(self, peg: Peg):
        """ gets a list of lists [[Point, Point],...] based on 
            get_possible_bridge_nodes_from_peg that validates that the other 
            end as possible. It does not validate intersection with other bridges.
        """
        return_list = []
        for p in self.get_possible_bridge_endpoints_from_peg(peg):
            return_list.append([peg, p])

        return return_list

    def did_win(self) -> bool:
        """ determines if this player won by getting a 

        Returns:
            bool: T/F whether this player won.
        """

        def find_path(start, end, path=[]):
            graph = self._pieces._piece_list
            path = path + [start]
            if start == end:
                return path
            if start not in graph.keys():
                return None
            for node in graph[start]:
                if node not in path:
                    new_path = find_path(node, end, path)
                    if new_path: return new_path
            return None

        #get a list of all pegs on the 0/1 side and 23/24 side.
        low_pegs = self._filter_pegs([0,1])
        high_pegs = self._filter_pegs([22,23])

        # iterate over all and see if there is a win.
        for low_peg in low_pegs:
            for high_peg in high_pegs:
                if find_path(low_peg, high_peg) is not None:
                    return True

        return False        

    def _filter_pegs(self, values):
        filter_list = []
        for peg in self.get_pegs():
            if self._direction == constants.DIRECTION_LEFT_RIGHT:
                if peg.get_position().get_x() in values:
                    filter_list.append(peg)
            elif self._direction == constants.DIRECTION_UP_DOWN:
                if peg.get_position().get_y() in values:
                    filter_list.append(peg)

        return filter_list

    def get_direction(self):
        return self._direction

    def set_network(self, network_status):
        self.network_service = NetworkService(self.IPADDRESS,self.PORT, network_status)
        self.client_server = network_status
