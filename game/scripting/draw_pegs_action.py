from game.scripting.action import Action
from game.casting.peg import Peg
from game.casting.player import Player
from game.casting.circle import Circle
from game.casting.cast import Cast
from game.services.video_service import VideoService

import constants

class DrawPegsAction(Action):
    """ The responsibility of DrawPegs is to draw all pegs from all player objects.
    """
    def __init__(self, video_service: VideoService) -> None:
        """initialization of the object

        Args:
            video_service (VideoService): An instance of Video Service.
        """
        super().__init__()
        self._video_service = video_service

    def execute(self, cast: Cast, script, callback):
        """ walk each player (including the preview player) and use the video service to draw the pegs.

        Args:
            cast: An instance of Cast containing the actors in the game.
            script: An instance of Script containing the actions in the game.
            callback: An instance of ActionCallback so we can change the scene.
        """

        players = cast.get_actors(constants.PLAYERS_GROUP) 
        preview_player = cast.get_first_actor(constants.PREVIEW_GROUP)
        if preview_player is not None:
            players.append(preview_player)

        for player in players:
            for point in player.get_peg_locations():
                circle = Circle(point,constants.PEG_RADIUS)
                
                self._video_service.draw_circle(circle, player.get_color(), filled=True)
