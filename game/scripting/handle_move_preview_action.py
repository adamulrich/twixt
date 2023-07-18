from constants import *
from game.casting.cast import Cast
from game.casting.peg import Peg
from game.casting.point import Point
from game.casting.player import Player
from game.casting.actor import Actor
from game.services.mouse_service import MouseService
from game.scripting.helper_functions import *


from game.scripting.action import Action


class HandleMovePreviewAction(Action):
    """ The responsibility of HandleMovePreview is to add potential pegs and bridges to the preview player, then add 
            the preview player to the cast, when the mouse is hovering over a hole.
    """
    
    def __init__(self, video_service, mouse_service: MouseService) -> None:
        """initialization of the object

        Args:
            video_service (VideoService): An instance of Video Service.
            mouse_service (MouseService): An instance of MouseService.
        """
        super().__init__()
        self._video_service = video_service
        self._mouse_service = mouse_service
        player_colors = {constants.RED: constants.LIGHT_RED, constants.BLACK: constants.GREY}

    def execute(self, cast: Cast, script, callback):
        """ this function should add potential pegs and bridges to the preview player, then add 
            the preview player to the cast, when the mouse is hovering over a hole.

        Args:
            cast: An instance of Cast containing the actors in the game.
            script: An instance of Script containing the actions in the game.
            callback: An instance of ActionCallback so we can change the scene.
        """

        #if it's not a network game
        player: Player = cast.get_first_actor(constants.CURRENT_PLAYER_GROUP)
        if player.client_server == NETWORK_NONE or player.me:
        

            # get the empty holes
            holes: list[Actor] = cast.get_actors(constants.HOLES_GROUP)

            #clear the preview group
            cast.clear_actors(constants.PREVIEW_GROUP)

            # get the list of holes, and check for mouse over.
            for hole in holes:
                if self._is_mouse_over(hole.get_screen_position()):

                    #check for valid location for this player
                    direction = player.get_direction()
                    if  constants.MIN_X[direction] <= hole.get_position().get_x() <= constants.MAX_X[direction] \
                        and constants.MIN_Y[direction] <= hole.get_position().get_y() <= constants.MAX_Y[direction]:

                        #create a new peg, add it to the preview player
                        preview_player = Player(constants.PREVIEW_COLORS[player.get_color()],player.get_direction())
                        peg = Peg(constants.PREVIEW_COLORS[player.get_color()], player.get_direction(), hole.get_position())
                        preview_player.add_peg(peg)                    
        
                        # find the potential bridges, add them to the preview player
                        create_bridges = get_potential_bridge_list(cast, player, peg)

                        if len(create_bridges) > 0  :
                            for bridge in create_bridges:
                                preview_player.add_bridge(bridge[0], bridge[1])

                        # add the preview player to the cast
                        cast.add_actor(constants.PREVIEW_GROUP,preview_player)
                        break


    def _is_mouse_over(self, hole: Actor):
        """determines if the mouse is over a hole

        Args:
            hole (Actor): _description_

        Returns:
            _type_: _description_
        """

        #get the min and max for the hole
        min_x = hole.get_x() - int(constants.SCREEN_SCALE/2)
        min_y = hole.get_y() - int(constants.SCREEN_SCALE/2)
        
        max_x = min_x + constants.SCREEN_SCALE - 1
        max_y = min_y + constants.SCREEN_SCALE - 1

        #get current mouse position
        position: Point = self._mouse_service.get_coordinates()

        if (min_x <= position.get_x()  <= max_x) and (min_y <= position.get_y() <= max_y):
            return True
        else:
            return False

