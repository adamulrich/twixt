from game.casting.point import Point


class Circle:
    """A Circle. All points equidistant from a single point.
    
    The responsability of Circle is to be placed on the board.
    
    Attributes:
        _center: the center point of the circle
        _radius: the radius of the circle"""

    def __init__(self, center: Point, radius: int):
        """Constructs a new Rectangle."""
        self._center = center
        self._radius = radius

    def get_center(self) -> Point:
        """Gets the top left point of the rectangle.
        
        Returns:
            An instance of Point containing the top left coordinates.
        """
        return self._center

    def get_radius(self) -> int:
        """Gets the size of the rectangle.
        
        Returns:
            An instance of Point containing the width and height.
        """
        return self._radius
