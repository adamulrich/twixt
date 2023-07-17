import constants
from game.casting.cast import Cast
from game.casting.peg import Peg
from game.casting.point import Point
from game.casting.player import Player
from game.casting.actor import Actor
from game.services.mouse_service import MouseService
from game.services.network_service import NetworkService

from game.scripting.action import Action

class DrawNetworkWaitingAction(Action):
    """ The responsibility of HandleMouseClick is to add a new peg to the New_Peg group if a mouse click happened on 
        a valid hole. It then removes the hole from the hole group
    """

    def execute(self, cast: Cast, script, callback):

        #if it is a network game, and we are waiting, then draw waiting message

        current_player: Player = cast._current_player
        if not current_player.current_turn:
            status: Actor = cast.get_first_actor(constants.STATUS_GROUP)
            status.set_text("Waiting on other player")
            status.set_color(current_player.get_color())