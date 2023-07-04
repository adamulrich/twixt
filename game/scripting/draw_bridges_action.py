from game.scripting.action import Action
from game.casting.player import Player
from game.casting.point import Point
from game.casting.cast import Cast
from game.services.video_service import VideoService
import constants


class DrawBridgesAction(Action):
    """    
    The responsibility of DrawBridges is to draw all bridges in each player object
    """
    

    def __init__(self, video_service: VideoService) -> None:
        """initialization of the object

        Args:
            video_service (VideoService): An instance of Video Service.
        """
        super().__init__()
        self._video_service = video_service

    def execute(self, cast: Cast, script, callback):
        """draw all bridges from each player object.

        Args:
            cast: An instance of Cast containing the actors in the game.
            script: An instance of Script containing the actions in the game.
            callback: An instance of ActionCallback so we can change the scene.
        """

        players: list[Player] = cast.get_actors(constants.PLAYERS_GROUP) 
        preview_player = cast.get_first_actor(constants.PREVIEW_GROUP)
        thickness: float = 8
        if preview_player is not None:
            players.append(preview_player)
        for player in players:
            for bridge in player.get_bridges():

                self._video_service.draw_line_ex(
                                    bridge[0].get_screen_position(), 
                                    bridge[1].get_screen_position(), 
                                    thickness, 
                                    player.get_color())
