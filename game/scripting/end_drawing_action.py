from game.scripting.action import Action


class EndDrawingAction(Action):
    """ The responsibility of EndDrawing is to flush the display buffer so that the screen is painted.
    

    Args:
        _video_service: An instance of VideoService
    """
    def __init__(self, video_service):
        """initialization of the object

        Args:
            video_service (VideoService): An instance of Video Service.
        """
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        """flushes the buffer

        Args:
            cast: An instance of Cast containing the actors in the game.
            script: An instance of Script containing the actions in the game.
            callback: An instance of ActionCallback so we can change the scene.
        """
        self._video_service.flush_buffer()