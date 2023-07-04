import constants
from game.scripting.action import Action
from game.casting.cast import Cast
from game.casting.player import Player
from game.casting.point import Point
from game.casting.peg import Peg
from game.scripting.helper_functions import *

class AddAllPossibleBridgesAction(Action):
    """ it is the responsibility of this action to add all possible bridges based on the latest peg
        added to the board to the current player object

    Args:
        Action (Action): An Instance of Action
    """ 

    def execute(self, cast: Cast, script, callback):
        """ if a new peg exists, it determines the current player, then determines if there
            are any new bridges that can be added to that new peg based on existing pegs.  

        Args:
            cast (Cast): An instance of Cast.
            script (Script): An instance of Script.
            callback (function): 
        """

        # if there is a new peg.
        new_peg: Peg = cast.get_first_actor(constants.NEW_PEG_GROUP)
        if new_peg is not None:

            # get the current player and find any potential bridges.
            player: Player = cast.get_first_actor(constants.CURRENT_PLAYER_GROUP)
            create_bridges = get_potential_bridge_list(cast, player, new_peg)

            # if there are new ones, add them.
            if len(create_bridges) > 0  :
                for bridge in create_bridges:
                    player.add_bridge(bridge[0], bridge[1])
            



        