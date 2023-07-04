from game.scripting.action import Action


class ReleaseDevicesAction(Action):
    """It is the responsibility of ReleaseDevicesAction to release any devices needed.
    """


    def __init__(self, video_service):
        """initialization of the object

        Args:
            video_service (VideoService): An instance of Video Service.
        """

        self._video_service = video_service

    def execute(self, cast, script, callback):
        """ release any devices needed.

        Args:
            cast: An instance of Cast containing the actors in the game.
            script: An instance of Script containing the actions in the game.
            callback: An instance of ActionCallback so we can change the scene.
        """

        self._video_service.release()