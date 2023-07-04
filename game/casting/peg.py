import constants
from game.casting.actor import Actor
from game.casting.point import Point

directions = [[1,2],[1,-2],[-1,2],[-1,-2],[2,1], [2,-1],[-2,1],[-2,-1]]

class Peg(Actor):
    """ a peg is a piece on the board. 
    The responsibility of peg is to keep track of a peg and it's properties, as well
    as to calculate the possible locations for other pegs that could be bridged to this peg.

    Args:
        Actor (_type_): _description_
    """

    def __init__(self, color, direction, position):
        """ initializes the peg

        Args:
            color (Color): An instance of Color
            direction (direction_constant): 0/1 depending on whether this player is going left/right or up/down
            position (Point): The grid position of the peg
        """
        super().__init__(position, "", color)
        self._direction = direction
        self._position_text = f"{self._position.get_x()},{self._position.get_y()} " 

    def get_possible_bridge_endpoints_on_board(self) -> list[Actor]:
        """ returns a list of possible locations that are on the board that this peg could be bridged to.
            It does not look at existing pegs or bridges.

        Return: list[Peg]
        """
        # returns all possible bridge endpoints from this peg that are on the board
        return_list = []
        x = self._position.get_x()
        y = self._position.get_y()

        # walk the list of directions and find valid locations
        for direction in directions:
            new_x = x + direction[0]
            new_y = y + direction[1]
            # is it on the board.
            if new_x >= constants.MIN_X[self._direction] and new_x <= constants.MAX_X[self._direction] and \
            new_y >= constants.MIN_Y[self._direction] and new_y <= constants.MAX_Y[self._direction]:
                return_list.append(Peg(self.get_color(),self._direction,Point(new_x,new_y)))

        return(return_list)



    
