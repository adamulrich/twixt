from constants import *
from game.casting.cast import Cast
from game.directing.scene_manager import SceneManager
from game.scripting.action_callback import ActionCallback
from game.scripting.script import Script


class Director(ActionCallback):
    """A person who directs the game.
    
    the responsibility of the director is to direct the game.
    
    Args:
        video_service (VideoService): An instance of VideoService.
        _cast: an instance of Cast
        _script: an instance of Script
        _scene_manager: an instance of SceneManager """

    def __init__(self, video_service, network_status):
        """Constructs a new Director using the specified video service.
        """

        self._video_service = video_service
        self._cast = Cast()
        self._script = Script()
        self._scene_manager = SceneManager(network_status)

        
    def on_next(self, scene):
        """Overriden ActionCallback method transitions to next scene.
        
        Args:
            A number representing the next scene to transition to.
        """
        self._scene_manager.prepare_scene(scene, self._cast, self._script)
        
    def start_game(self):
        """Starts the game. Runs the main game loop."""

        self.on_next(NEW_GAME)
        self._execute_actions(INITIALIZE)
        self._execute_actions(LOAD)
        while self._video_service.is_window_open():
            self._execute_actions(INPUT)
            self._execute_actions(UPDATE)
            self._execute_actions(OUTPUT)
        self._execute_actions(UNLOAD)
        self._execute_actions(RELEASE)
        
    def _execute_actions(self, group):
        """Calls execute for each action in the given group.
        
        Args:
            group (string): The action group name.
            cast (Cast): The cast of actors.
            script (Script): The script of actions.
        """
        actions = self._script.get_actions(group)    
        for action in actions:
            action.execute(self._cast, self._script, self)          
    

