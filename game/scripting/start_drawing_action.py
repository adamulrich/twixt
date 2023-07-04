from game.scripting.action import Action

class StartDrawingAction(Action):
    """ It is the responsibility of StartDrawingAction to 
        flush the video service buffer to start the next draw sequence.
    """
    
    def __init__(self, video_service):
        """initialization of the object

        Args:
            video_service (VideoService): An instance of Video Service.
        """

        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        """ clears the buffer so that we are ready for drawing.

        Args:
            cast: An instance of Cast containing the actors in the game.
            script: An instance of Script containing the actions in the game.
            callback: An instance of ActionCallback so we can change the scene.
        """

        self._video_service.clear_buffer()