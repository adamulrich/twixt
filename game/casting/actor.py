from game.casting.text import Text
import constants
from game.casting.color import Color
from game.casting.point import Point


class Actor:
    """A thing that participates in the game.

    The responsability of the actor is to participate in the game.

    Args:
            position (Point, optional): grid position for the Actor. Defaults to Point(0,0).
            text (str, optional): text for the Actor. Defaults to "".
            color (Color, optional): color of the Actor. Defaults to Color(255,255,255).

    """

    def __init__(self, position=Point(0, 0), text="", color=Color(255, 255, 255)):
        """ Initialization for an Actor
        """
        self._text = text
        self._color = color
        self._position = position

    def get_position(self):
        """getter for the Actor's position

        Returns:
            position: the actors position
        """
        return self._position

    def set_position(self, point: Point):
        """setter for the Actor's position

        Args:
            position (Point): point to set the Actor position
        """
        self._position = point

    def get_color(self):
        """getter for the Actor's color

        Returns:
            Color: The actor's color.
        """
        return self._color

    def set_color(self, color):
        """setter for the Actor's color

        Args:
            color (Color): color to set the Actors color
        """
        self._color = color

    def get_screen_position(self) -> Point:
        """ calculates the screen position from grid position based on Screen Scale

        Returns:
            Point: screen position for the Actor
        """
        x = (self._position.get_x() + 1) * constants.SCREEN_SCALE
        y = (self._position.get_y() + 1) * constants.SCREEN_SCALE
        return Point(x, y)

    def set_text(self, text):
        """ setter for the Actor text.

        Args:
            text (srt): text to set the Actor's text.
        """
        self._text = text

    def get_text(self):
        """ getter for the Actor's text

        Returns:
            str: Actor's text
        """
        return self._text
