from game.casting.circle import Circle
from game.casting.rectangle import Rectangle
from game.casting.point import Point
from game.casting.color import Color


class VideoService:
    """A video service interface."""

    def clear_buffer(self):
        """Prepares the buffer for drawing."""
        raise NotImplementedError("not implemented in base class")

    def draw_image(self, image, position):
        """Draws the given image on the buffer at the given position. The image won't appear
        on the screen until flush_buffer() is called.

        Args:
            image: An instance of batter.casting.image.
            position: An instance of batter.casting.point.

        Raises:
            KeyError: If the image file hasn't already been loaded.
        """
        raise NotImplementedError("not implemented in base class")

    def draw_rectangle(self, rectangle, color):
        """Draws a rectangle on the buffer at the given position. The rectangle won't appear
        on the screen until flush_buffer() is called.

        Args:
            size: An instance of batter.casting.point.
            position: An instance of batter.casting.point.
            color: An instance of batter.casting.color.
        """
        raise NotImplementedError("not implemented in base class")

    def draw_circle(self, circle, color, filled=False):
        """Draws a circle on the buffer at the given position. The rectangle won't appear
        on the screen until flush_buffer() is called.

        Args:
            radius: int representing the circle.
            position: An instance of Point.
            color: An instance of Color.
        """
        raise NotImplementedError("not implemented in base class")

    def draw_text(self, text, position, color):
        """Draws the given text on the buffer at the given position. The text won't appear
        on the screen until flush_buffer() is called.

        Args:
            text: An instance of batter.casting.text.
            position: An instance of batter.casting.point.

        Raises:
            KeyError: If the font file for the text hasn't already been loaded.
        """
        raise NotImplementedError("not implemented in base class")

    def flush_buffer(self):
        """Swaps the buffers, displaying everything that has been drawn on the screen."""
        raise NotImplementedError("not implemented in base class")

    def initialize(self):
        """Initializes underlying video device. This method should be called before the main game 
        loop begins."""
        raise NotImplementedError("not implemented in base class")

    def is_window_open(self):
        """Wether or not the window is open.

        Returns:
            True if the window is open; false if otherwise.
        """
        raise NotImplementedError("not implemented in base class")

    def load_fonts(self, directory):
        """Loads all the fonts in the given directory and sub-directories.

        Args:
            directory: A string containing the absolute folder path where font files are stored.
        """
        raise NotImplementedError("not implemented in base class")

    def load_images(self, directory):
        """Loads all the images in the given directory and sub-directories.

        Args:
            directory: A string containing the absolute folder path where image files are stored.
        """
        raise NotImplementedError("not implemented in base class")

    def release(self):
        """Releases the underlying video device. This method should be called after the game loop 
        has finished running."""
        raise NotImplementedError("not implemented in base class")

    def unload_fonts(self):
        """Unloads all fonts that were previously loaded."""
        raise NotImplementedError("not implemented in base class")

    def unload_images(self):
        """Unloads all images that were previously loaded."""
        raise NotImplementedError("not implemented in base class")

    def draw_line_with_rectangle(self, p1: Point, p2: Point, thickness: float, color: Color):
        """ draws a line using rectangle for the thickness of the line

        Args:
            p1 (Point): An instance of Point
            p2 (Point): An instance of Point
            thickness (float): the thickness for the line
            color (Color): An instance of Color
        """
        raise NotImplementedError("not implemented in base class")

    def draw_line_ex(self, p1: Point, p2: Point, thickness: float, color: Color):
        """ draw a line

        Args:
            p1 (Point): An instance of Point
            p2 (Point): An instance of Point
            thickness (float): the thickness for the line
            color (Color): An instance of Color
        """
        raise NotImplementedError("not implemented in base class")


