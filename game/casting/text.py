from constants import * 


class Text:
    """A text message.
    
    the responsability of the text is to give a message to the player.
    
    Attributes:
        _value: the value of the text
        _fontfile: the file that contains the font of the text
        _size: the size of the font
        _alignment: the alignment of the text
        _color: the color of the text"""

    def __init__(self, value, fontfile = FONT_FILE, size = FONT_LARGE, alignment = ALIGN_LEFT, color = BLACK):
        """Constructs a new Text."""
        self._value = value
        self._fontfile = fontfile
        self._size = size
        self._alignment = alignment
        self._color = color

    def get_alignment(self):
        """Gets the alignment for the text.
        
        Returns:
            A number representing the text alignment.
        """
        return self._alignment

    def get_fontfile(self):
        """Gets the font file for the text.
        
        Returns:
            A string containing the font file.
        """
        return self._fontfile

    def get_size(self):
        """Gets the font size of the text.
        
        Returns:
            A number representing the font size.
        """
        return self._size

    def get_value(self):
        """Gets the text's value.
        
        Returns:
            A string containing the text's value.
        """
        return self._value

    def set_value(self, value):
        """Sets the text's value.
        
        Args:
            A string containing the text's value.
        """
        self._value = value

    def get_color(self):
        """ getter for the color

        Returns:
            Color: the color of the text
        """
        return self._color 

    def set_color(self, color):
        """ setter for the color        

        Args:
            color (Color): the color to set for the text
        """
        self._color = color
