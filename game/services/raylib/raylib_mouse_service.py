import pyray
from game.casting.point import Point
from game.services.mouse_service import MouseService


class RaylibMouseService(MouseService):
    """ A Raylib implementation of MouseService."""

    def __init__(self):
        """initializes the raylib mouse service
        """
        self._buttons = {}
        self._buttons["left"] =  pyray.MOUSE_BUTTON_LEFT
        self._buttons["middle"] = pyray.MOUSE_BUTTON_MIDDLE
        self._buttons["right"] = pyray.MOUSE_BUTTON_RIGHT
    
    def get_coordinates(self):
        """getter for the current mouse coordinates

        Returns:
            Point: the current mouse coordinates
        """
        x = pyray.get_mouse_x()
        y = pyray.get_mouse_y()
        return Point(x, y)

    
    def is_button_pressed(self, button):
        """returns whether a mouse button is pressed

        Args:
            button (int): the button constant to check

        Returns:
            bool: True/False
        """
        raylib_button = self._buttons[button]
        return pyray.is_mouse_button_pressed(raylib_button)
        

