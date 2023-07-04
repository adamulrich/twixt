from game.scripting.action import Action
import constants
from game.casting.player import Player
from game.casting.cast import Cast
from game.casting.actor import Actor
from game.scripting.script import Script


class HandleWinAction(Action):
    """ The responsibility of HandleWin is to set the display message if the player has won, then stop the game.
    """

    def execute(self, cast: Cast, script: Script, callback):
        """ Sets the display message if the player has won, then stops the game.

        Args:
            cast: An instance of Cast containing the actors in the game.
            script: An instance of Script containing the actions in the game.
            callback: An instance of ActionCallback so we can change the scene.
        """

        player: Player = cast.get_next_player()

        if player.did_win():
            status: Actor = cast.get_first_actor(constants.STATUS_GROUP)
            status.set_text("Player Wins!")
            status.set_color(player.get_color())

            #remove the change action, and drop the input and update actions
            #script.remove_action(constants.UPDATE,script.get_actions(constants.UPDATE)[-1])
            script.clear_actions(constants.INPUT)
            script.clear_actions(constants.UPDATE)
