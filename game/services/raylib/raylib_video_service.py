import constants
import os
import math
import pathlib
import pyray
from constants import *
from game.casting.color import Color
from game.casting.point import Point
from game.casting.image import Image
from game.casting.text import Text
from game.services.video_service import VideoService 
from game.casting.rectangle import Rectangle
from game.casting.circle import Circle


class RaylibVideoService(VideoService):
    """ A Raylib implementation of VideoService."""

    def __init__(self, title = "", width = 640, height = 480, color = GREY):
        """initializes the Video Service

        Args:
            title (str, optional): Title of the Window. Defaults to "".
            width (int, optional): width of the window. Defaults to 640.
            height (int, optional): height of the window. Defaults to 480.
            color (_type_, optional): color of the window. Defaults to GREY.
        """
        self._title = title
        self._width = width
        self._height = height
        self._color = color
        self._fonts = {}
        self._textures = {}
        
    def initialize(self):
        """initializes the Video Service by creating a window
        """
                
        pyray.set_target_fps(60)
        pyray.init_window(self._width, self._height, self._title)
        pyray.set_trace_log_level(pyray.TraceLogLevel.LOG_WARNING)

    def is_window_open(self):
        """ determines of the window is still open.

        Returns:
            bool: whether the window is still open.
        """
        return not pyray.window_should_close()
        
    def clear_buffer(self):
        """clears the draw buffer
        """ 
        raylib_color = self._to_raylib_color(self._color)
        pyray.begin_drawing()
        pyray.clear_background(raylib_color)

    def draw_image(self, image: Image, position: Point):
        """ draws an image at the position

        Args:
            image (Image): An instance of Image
            position (Point): An instance of Point
        """
        filepath = image.get_filename()
        # fixed os dependent filepath
        filepath = str(pathlib.Path(filepath))
        texture = self._textures[filepath]
        x = position.get_x()
        y = position.get_y()
        raylib_position = pyray.Vector2(x, y)
        scale = image.get_scale()
        rotation = image.get_rotation()
        tint = self._to_raylib_color(Color(255,255,255)) 
        pyray.draw_texture_ex(texture, raylib_position, rotation, scale, tint)
         
    def draw_rectangle(self, rectangle: Rectangle, color: Color, filled = False):
        """ draws a rectangle

        Args:
            rectangle (Rectangle): An instance of Rectangle
            color (Color): An instance of Color
            filled (bool, optional): fill the rectangle with color t/f. Defaults to False.
        """
        x = int(rectangle.get_position().get_x())
        y = int(rectangle.get_position().get_y())
        width = int(rectangle.get_size().get_x())
        height = int(rectangle.get_size().get_y())
        raylib_color = self._to_raylib_color(color)

        if filled:
            pyray.draw_rectangle(x, y, width, height, raylib_color)
        else:
            pyray.draw_rectangle_lines(x, y, width, height, raylib_color)

    def draw_text(self, text: Text, position: Point, color: Color):
        """ draws text at the position provided, with the color provided

        Args:
            text (Text): The text to display
            position (Point): the location to draw at
            color (Color): the color for the text
        """
        value = text.get_value()
        size = text.get_size()
        spacing = 0
        alignment = text.get_alignment()
        tint = self._to_raylib_color(text.get_color())
        text_image = pyray.image_text(value,size,tint)
        
        x = position.get_x()
        y = position.get_y()

        if alignment == ALIGN_CENTER:
            x = int(position.get_x() - text_image.width / 2) 
        elif alignment == ALIGN_RIGHT:
            x = int(position.get_x() - text_image.width) 

        pyray.draw_text(value,x,y,size,tint)
        
    def flush_buffer(self):
        """ ends drawing
        """
        pyray.end_drawing()


    def load_fonts(self, directory):
        """ loads font files for use

        Args:
            directory (filepath): A filepath to a directory
        """
        filepaths = self._get_filepaths(directory, [".otf", ".ttf"])
        for filepath in filepaths:
            if filepath not in self._fonts.keys():
                font = pyray.load_font(filepath)
                self._fonts[filepath] = font

    def load_images(self, directory):
        """ loads images into an object so that they can be displayed

        Args:
            directory (filepath): A filepath to a directory of images
        """
        filepaths = self._get_filepaths(directory, [".png", ".gif", ".jpg", ".jpeg", ".bmp"])
        for filepath in filepaths:
            if filepath not in self._textures.keys():
                texture = pyray.load_texture(filepath)
                self._textures[filepath] = texture

    def release(self):
        """ closes a window
        """
        pyray.close_window()
        
    def unload_fonts(self):
        """ unloads fonts
        """
        for font in self._fonts.values():
            pyray.unload_font(font)
        self._fonts.clear()

    def unload_images(self):
        """ unloads images
        """
        for texture in self._textures.values():
            pyray.unload_texture(texture)
        self._textures.clear()

    def _get_filepaths(self, directory, filter):
        """gets filepaths for all the files represented by the filter value

        Args:
            directory (filepath): a filepath
            filter (str): a list of *. extensions to look for

        Returns:
            list[filepaths]
        """
        filepaths = []
        for file in os.listdir(directory):
            filename = os.path.join(directory, file)
            extension = pathlib.Path(filename).suffix.lower()
            if extension in filter:
                filename = str(pathlib.Path(filename))
                filepaths.append(filename)
        return filepaths

    def _to_raylib_color(self, color: Color):
        """ turns a Color object into a pyray Color object

        Args:
            color (Color): An instance of Color

        Returns:
            Pyray Color struct
        """
        r, g, b, a = color.to_tuple()
        return pyray.Color(r, g, b, a)

    def draw_circle(self, circle: Circle, color, filled = False):
        """ draws a circle

        Args:
            circle (Circle): An instance of Circle
            color (Color): An instance of Color
            filled (bool, optional): Whether to fill the circle with the color. Defaults to False.
        """
        x = int(circle.get_center().get_x())
        y = int(circle.get_center().get_y())
        radius = int(circle.get_radius())
        raylib_color = self._to_raylib_color(color)

        if filled:
            pyray.draw_circle(x, y, radius, raylib_color)
        else:
            pyray.draw_circle_lines(x, y, radius, raylib_color)

    def draw_line_with_rectangle(self, p1: Point, p2: Point, thickness: float, color: Color):
        """ draws a line using rectangle for the thickness of the line

        Args:
            p1 (Point): An instance of Point
            p2 (Point): An instance of Point
            thickness (float): the thickness for the line
            color (Color): An instance of Color
        """
       
        width = (p1.get_x() - p2.get_x())
        height = (p1.get_y() - p2.get_y())

        offset = 180 if width >= 0 else 0
        length = int(math.sqrt(width**2 + height**2))

        rotation = math.atan( height/width) * 180/math.pi + offset

        raylib_color = self._to_raylib_color(color)
        rec = pyray.Rectangle(p1.get_x(),p1.get_y(),length, thickness)

        pyray.draw_rectangle_pro(rec, pyray.Vector2(0,abs(int(thickness/2))), rotation, raylib_color)
        
    def draw_line_ex(self, p1: Point, p2: Point, thickness: float, color: Color):
        """ draw a line

        Args:
            p1 (Point): An instance of Point
            p2 (Point): An instance of Point
            thickness (float): the thickness for the line
            color (Color): An instance of Color
        """
        v1 = pyray.Vector2(p1.get_x(), p1.get_y())
        v2 = pyray.Vector2(p2.get_x(), p2.get_y())
        raylib_color = self._to_raylib_color(color)
        pyray.draw_line_ex(v1, v2, thickness, raylib_color)
