from game.scripting.action import Action
from game.casting.peg import Peg
from game.casting.player import Player
from game.casting.actor import Actor
from game.casting.circle import Circle
from game.casting.point import Point
from game.casting.cast import Cast
from game.casting.text import Text
from game.services.video_service import VideoService
import constants
import math

class DrawBoardAction(Action):
    """ The Responsibility of DrawBoard is the use the video service to draw the board.
    """
    def __init__(self, video_service:VideoService) -> None:
        """initialization of the object

        Args:
            video_service (VideoService): An instance of Video Service.
        """
        super().__init__()
        self._video_service = video_service


    def execute(self, cast: Cast, script, callback):
        """use the video service to draw the board: holes, lines and status.

        Args:
            cast: An instance of Cast containing the actors in the game.
            script: An instance of Script containing the actions in the game.
            callback: An instance of ActionCallback so we can change the scene.
        """
        scale = constants.SCREEN_SCALE
        for hole in cast.get_actors(constants.HOLES_GROUP):
               circle = Circle(hole.get_screen_position(), constants.PEG_RADIUS)
               self._video_service.draw_circle(circle, constants.DARK_SLATE_GREY,filled=True )

        #draw lines
        thickness = 4
        x1 = ((1) * constants.SCREEN_SCALE) +  int(constants.SCREEN_SCALE/2)
        x2 = ((22+ 1) * constants.SCREEN_SCALE) +  int(constants.SCREEN_SCALE/2)
        y1 = (1+ 1) * constants.SCREEN_SCALE
        y2 = (22 + 1) * constants.SCREEN_SCALE

        self._video_service.draw_line_ex(Point(x1,y1),Point(x1,y2), thickness, constants.RED)
        self._video_service.draw_line_ex(Point(x2,y1),Point(x2,y2), thickness, constants.RED)

        self._video_service.draw_line_ex(Point(y1,x1),Point(y2,x1), thickness, constants.BLACK)
        self._video_service.draw_line_ex(Point(y1,x2),Point(y2,x2), thickness, constants.BLACK)

        #draw message
        status: Actor = cast.get_first_actor(constants.STATUS_GROUP)
        text = Text(status.get_text(),constants.FONT_FILE,alignment=constants.ALIGN_CENTER, color=status.get_color())
        self._video_service.draw_text(text, status.get_screen_position(), status.get_color())

   
        