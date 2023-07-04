from game.casting.actor import Actor
from game.casting.peg import Peg
from game.casting.point import Point
import typing


class Pieces():
    """ Pieces is the different pieces of the game.
    
    it is the responsibility of Pieces to keep track of all the pieces on the board for a particular player

    Attributes:
        _piece_list (dict): the dictionary of pieces.
    """

    def __init__(self) -> None:
        """ initializes the pieces object
        """
        
        self._piece_list = {}


    def add_peg(self, peg):
        """ add a peg to the piece list

        Args:
            peg (Peg): An instance of Peg
        """
        self._piece_list[peg] = []

    def add_bridge(self, peg1: Peg, peg2: Peg):
        """ add a bridge by adding it's end points to the value lists of the
            keys of the opposite end point.

        Args:
            peg1 (Peg): An instance of Peg
            peg2 (Peg): An instance of Peg
        """
        
        if peg1 in self._piece_list.keys():    
            self._piece_list[peg1].append(peg2)
        
        if peg2 in self._piece_list.keys():
            self._piece_list[peg2].append(peg1)

    def get_peg_list(self) -> list[Peg]:
        """getter for the peg list

        Returns:
            list[Peg]: a list of the pegs in this piece object
        """
        return list(self._piece_list.keys())

    def get_bridge_list(self) -> list[list[Peg]]:
        """ returns a list of the bridges by providing a list of lists. Each inner list
            is a pair of pegs

        Returns:
            list of lists: [[peg1, peg2], ...]
        """
        return_list = []
        # get all the pegs and create the list
        for peg1, peg_list in self._piece_list.items():
            for peg2 in peg_list:
                append_flag = True
                for bridge in return_list:
                    if bridge[0] == peg2 and bridge[1] == peg1:
                        append_flag = False
                        break
                if append_flag:
                    return_list.append([peg1,peg2])
        
        # the list is duplicated. need to deduplicate it.
        return return_list
