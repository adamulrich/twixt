from constants import *
from game.casting.cast import Cast
from game.casting.peg import Peg
from game.casting.point import Point
from game.casting.player import Player
from game.casting.actor import Actor
from game.services.mouse_service import MouseService
from game.services.network_service import NetworkService

from game.scripting.action import Action

class HandleNetworkMouseClickAction(Action):
    """ The responsibility of HandleMouseClick is to add a new peg to the New_Peg group if a mouse click happened on 
        a valid hole. It then removes the hole from the hole group
    """
    def __init__(self, mouse_service: MouseService) -> None:
        """initialization of the object

        Args:
            mouse_service (MouseService): An instance of MouseService.
        """
        super().__init__()
        self._mouse_service = mouse_service

    def execute(self, cast: Cast, script, callback):
        """ HandleMouseClick adds a new peg to the New_Peg group if a mouse click happened on 
            a valid hole. Then remove the hole from the hole group

        Args:
            cast: An instance of Cast containing the actors in the game.
            script: An instance of Script containing the actions in the game.
            callback: An instance of ActionCallback so we can change the scene.
        """
        player: Player = cast.get_first_actor(CURRENT_PLAYER_GROUP)


        # if it is our turn we get the data
        if player.client_server != NETWORK_NONE:
            if player.me:
            
                #if the mouse button is pressed
                if self._mouse_service.is_button_pressed('left'):

                    #get position
                    position: Point = self._mouse_service.get_coordinates()


                    # get the empty holes
                    holes: list[Actor] = cast.get_actors(HOLES_GROUP)

                    #translate this to a location for a hole
                    for hole in holes:
                        if self._is_mouse_over(hole.get_screen_position(), position):

                            #check for valid location for this player
                            direction = player.get_direction()
                            if  MIN_X[direction] <= hole.get_position().get_x() <= MAX_X[direction] \
                                and MIN_Y[direction] <= hole.get_position().get_y() <= MAX_Y[direction]:

                                #remove hole from hole list
                                cast.remove_actor(HOLES_GROUP,hole)

                                #create a new peg, add it to the new hole group
                                peg = Peg(player.get_color(), player.get_direction(), hole.get_position())
                                cast.add_actor(NEW_PEG_GROUP,peg)

                                # send data to other player
                                player.network_service.send_data(position)

                                break
            else:
                next_player: Player = cast.get_next_player()
                position = next_player.network_service.get_data()
                if position:

                    # get the empty holes
                    holes: list[Actor] = cast.get_actors(HOLES_GROUP)

                    #translate this to a location for a hole
                    for hole in holes:
                        if self._is_mouse_over(hole.get_screen_position(), position):

                            #check for valid location for this player
                            direction = player.get_direction()
                            if  MIN_X[direction] <= hole.get_position().get_x() <= MAX_X[direction] \
                                and MIN_Y[direction] <= hole.get_position().get_y() <= MAX_Y[direction]:

                                #remove hole from hole list
                                cast.remove_actor(HOLES_GROUP,hole)

                                #create a new peg, add it to the new hole group
                                peg = Peg(player.get_color(), player.get_direction(), hole.get_position())
                                cast.add_actor(NEW_PEG_GROUP,peg)

                                break



    def _is_mouse_over(self, hole: Actor, position: Point):
        """determines if the mouse is over a hole

        Args:
            hole (Actor): _description_

        Returns:
            _type_: _description_
        """

        #get the min and max for the hole
        min_x = hole.get_x() - int(SCREEN_SCALE/2)
        min_y = hole.get_y() - int(SCREEN_SCALE/2)
        
        max_x = min_x + SCREEN_SCALE - 1
        max_y = min_y + SCREEN_SCALE - 1

        #get current mouse position

        if (min_x <= position.get_x()  <= max_x) and (min_y <= position.get_y() <= max_y):
            return True
        else:
            return False
