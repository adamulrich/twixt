import constants
from game.scripting.action import Action
from game.casting.cast import Cast
from game.casting.player import Player
from game.casting.point import Point
from game.casting.peg import Peg
class AddPegAction(Action):
    """This adds a peg to the board.

    Args:
        Action (Action): An Instance of Action
    """

    def execute(self, cast: Cast, script, callback):
        """ add a peg to the current Actor object if there is a new peg in 
            the new peg collection, then clear the preview group.
            
        Args:
            cast: An instance of Cast containing the actors in the game.
            script: An instance of Script containing the actions in the game.
            callback: An instance of ActionCallback so we can change the scene.
        """
        
        #check to see if there is a new peg in the new peg group
        new_peg: Peg = cast.get_first_actor(constants.NEW_PEG_GROUP)
        if new_peg is not None:

        #if new peg then add it to the current players peg list
            player: Player = cast.get_first_actor(constants.CURRENT_PLAYER_GROUP)
            player.add_peg(new_peg)

            #clear the preview group
            cast.clear_actors(constants.PREVIEW_GROUP)
        