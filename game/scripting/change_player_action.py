import constants
from game.casting.cast import Cast
from game.casting.peg import Peg
from game.casting.point import Point
from game.casting.player import Player
from game.casting.actor import Actor
from game.services.mouse_service import MouseService

from game.scripting.action import Action

class ChangePlayerAction(Action):
    """A thing that is done.
    
    The responsibility of ChangePlayer is to update the current player group to the next player and
            updates the status message to point to the current player.
    """

    def execute(self, cast: Cast, script, callback):
        """ ChangePlayer updates the current player group to the next player and
            updates the status message to point to the current player.

        Args:
            cast: An instance of Cast containing the actors in the game.
            script: An instance of Script containing the actions in the game.
            callback: An instance of ActionCallback so we can change the scene.
        """
        # remove the from the new_peg group
        new_peg = cast.get_first_actor(constants.NEW_PEG_GROUP)
        if new_peg is not None:
            cast.remove_actor(constants.NEW_PEG_GROUP,new_peg)

            # swap current player
            current_player: Player = cast.get_first_actor(constants.CURRENT_PLAYER_GROUP)
            new_player = None

            for player in cast.get_actors(constants.PLAYERS_GROUP):
                if player is not current_player:
                    new_player: Player = player
                    cast.remove_actor(constants.CURRENT_PLAYER_GROUP,current_player)
                    cast.add_actor(constants.CURRENT_PLAYER_GROUP,player)
                    break
            
            status: Actor = cast.get_first_actor(constants.STATUS_GROUP)
            status.set_text(constants.STATUS_MESSAGE[new_player.get_direction()])
            status.set_color(new_player.get_color())
