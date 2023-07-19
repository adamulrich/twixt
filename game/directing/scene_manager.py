import csv
import socket
from constants import *
from game.casting.label import Label
from game.casting.point import Point
from game.casting.cast import Cast
from game.casting.text import Text
from game.casting.player import Player
from game.casting.actor import Actor
from game.scripting.script import Script
from game.services.raylib.raylib_video_service import RaylibVideoService
from game.services.raylib.raylib_mouse_service import RaylibMouseService
from game.scripting.initialize_devices_action import InitializeDevicesAction
from game.scripting.start_drawing_action import StartDrawingAction
from game.scripting.draw_board_action import DrawBoardAction
from game.scripting.draw_bridges_action import DrawBridgesAction
from game.scripting.draw_pegs_action import DrawPegsAction
from game.scripting.end_drawing_action import EndDrawingAction
from game.scripting.add_all_possible_bridges_action import AddAllPossibleBridgesAction
from game.scripting.add_peg_action import AddPegAction
from game.scripting.handle_mouse_click_action import HandleMouseClickAction
from game.scripting.handle_move_preview_action import HandleMovePreviewAction
from game.scripting.handle_win_action import HandleWinAction
from game.scripting.release_devices_action import ReleaseDevicesAction
from game.scripting.change_player_action import ChangePlayerAction
from game.services.network_service import NetworkService
from game.scripting.handle_network_mouse_click_action import HandleNetworkMouseClickAction

class SceneManager:
    """The person in charge of setting up the cast and script for each scene."""

    MOUSE_SERVICE = RaylibMouseService()
    VIDEO_SERVICE = RaylibVideoService(GAME_NAME, SCREEN_WIDTH, 1000)


    INITIALIZE_DEVICES_ACTION = InitializeDevicesAction(VIDEO_SERVICE)

    HANDLE_MOUSE_CLICK_ACTION = HandleMouseClickAction(MOUSE_SERVICE)
    ADD_PEG_ACTION = AddPegAction()
    ADD_ALL_POSSIBLE_BRIDGES_ACTION = AddAllPossibleBridgesAction()
    CHANGE_PLAYER_ACTION = ChangePlayerAction()
    HANDLE_WIN_ACTION = HandleWinAction()
    HANDLE_MOVE_PREVIEW_ACTION = HandleMovePreviewAction(VIDEO_SERVICE, MOUSE_SERVICE)
    HANDLE_NETWORK_MOUSE_CLICK_ACTION = HandleNetworkMouseClickAction(MOUSE_SERVICE)


    START_DRAWING_ACTION = StartDrawingAction(VIDEO_SERVICE)
    

    DRAW_BOARD_ACTION = DrawBoardAction(VIDEO_SERVICE)
    DRAW_BRIDGES_ACTION = DrawBridgesAction(VIDEO_SERVICE)
    DRAW_PEGS_ACTION = DrawPegsAction(VIDEO_SERVICE)
    END_DRAWING_ACTION = EndDrawingAction(VIDEO_SERVICE)
    
    RELEASE_DEVICES_ACTION = ReleaseDevicesAction( VIDEO_SERVICE)
    

    def __init__(self, network_status, ip_address):
        """ Initialization for a SceneManager"""
        self.network_status = network_status
        self.ip_address = ip_address

    def prepare_scene(self, scene, cast: Cast, script: Script):
        """Prepares the scene that corresponds to a number

    
        Args:
            scene: A number that is saved to a scene of the game
            cast (Cast): an instance of Cast 
            script (Script): an instance of Script
        """
        if scene == NEW_GAME:
            self._prepare_new_game(cast, script)
        elif scene == TRY_AGAIN:
            self._prepare_try_again(cast, script)
        elif scene == IN_PLAY:
            self._prepare_in_play(cast, script)
        elif scene == GAME_OVER:
            self._prepare_game_over(cast, script)




    # ----------------------------------------------------------------------------------------------
    # scene methods
    # ----------------------------------------------------------------------------------------------

    def _prepare_new_game(self, cast: Cast, script: Script):
        """Prepares a new game

        Args:
            cast (Cast): an instance of Cast 
            script (Script): an instance of Script
        """
        self._add_players(cast)
        self._add_board(cast)
        self._add_dialog(cast, ENTER_TO_START)

        self._add_initialize_script(script)

        self._add_input_script(script)
        self._add_output_script(script)
        self._add_update_script(script)

        self._add_release_script(script)
    
    def _prepare_game_over(self, cast: Cast, script: Script):
        """Prepares the game over scene

        Args:
            cast (Cast): an instance of Cast 
            script (Script): an instance of Script
        """
        self._add_dialog(cast, WAS_GOOD_GAME)

        script.clear_actions(INPUT)
        script.clear_actions(UPDATE)
        self._add_output_script(script)

    # ----------------------------------------------------------------------------------------------
    # casting methods
    # ----------------------------------------------------------------------------------------------
    def _add_players(self, cast: Cast):
        """Adds players to the game

        Args:
            cast (Cast): an instance of Cast 
        """
        cast.clear_actors(PLAYERS_GROUP)
        player_data =  [[RED, DIRECTION_LEFT_RIGHT], [BLACK, DIRECTION_UP_DOWN]]

        for player in player_data:
            players = Player(color = player[0], direction = player[1])
            cast.add_actor(PLAYERS_GROUP, players)

        #set the current actor
        cast.add_actor(CURRENT_PLAYER_GROUP,cast.get_first_actor(PLAYERS_GROUP))

        #set the network up in the player if it is a network game.
        if self.network_status == NETWORK_SERVER:
            #set server player 
            player: Player = cast.get_first_actor(CURRENT_PLAYER_GROUP)
            player.set_network(NETWORK_SERVER)
            player.current_turn = True
            player.me = True

            #set client player
            player: Player = cast.get_next_player()
            player.client_server = NETWORK_CLIENT
            player.current_turn = False
            player.IPADDRESS = self.ip_address


        if self.network_status == NETWORK_CLIENT:

            #set client player
            player: Player = cast.get_next_player()
            player.set_network(NETWORK_CLIENT)
            player.current_turn = False
            player.me = True

            #set server player
            player: Player = cast.get_first_actor(CURRENT_PLAYER_GROUP)
            player.current_turn = True
            player.client_server = NETWORK_SERVER
            player.me = False

        if self.network_status == NETWORK_NONE:
            player: Player = cast.get_first_actor(CURRENT_PLAYER_GROUP)
            player.current_turn = True
            player.client_server = NETWORK_NONE


    def _add_dialog(self, cast: Cast, message):
        """Adds dialog to the game

        Args:
            cast (Cast): an instance of Cast 
            message: A message that will be shown as dialog
        """
        cast.clear_actors(DIALOG_GROUP)
        text = Text(message, FONT_FILE, FONT_SMALL, ALIGN_CENTER)
        position = Point(CENTER_X, CENTER_Y)
        label = Label(text, position)
        cast.add_actor(DIALOG_GROUP, label)

    def _add_board(self, cast: Cast):
        """Adds the board

        Args:
            cast (Cast): an instance of Cast
        """
        except_list = [(0, 0), (0, 23), (23, 0), (23, 23)]
        for i in range(0, 24):
            for j in range(0, 24):
                if (i, j) not in except_list:
                    hole = Actor(position=Point(i,j))
                    cast.add_actor(HOLES_GROUP, hole)

        
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        #set up which player you are for network game
        if self.network_status == NETWORK_SERVER:
                text =f"RED: {hostname}, {ip_address}"
                cast.add_actor(PLAYER_COLOR_STATUS_GROUP, Actor(text=text,position=Point(19,26),color=RED))        
                
        if self.network_status == NETWORK_CLIENT:
                text =f"BLACK: {hostname}, {ip_address}"
                cast.add_actor(PLAYER_COLOR_STATUS_GROUP, Actor(text=text,position=Point(19,26),color=BLACK))   
        

        cast.add_actor(STATUS_GROUP, Actor(text=RED_PLAYERS_TURN,position= Point(15,24),color=RED) )

    # ----------------------------------------------------------------------------------------------
    # scripting methods
    # ----------------------------------------------------------------------------------------------
    def _add_initialize_script(self, script: Script):
        """Add the initialize scene to the script

        Args:
            script (Script): an instance of Script
        """
        script.clear_actions(INITIALIZE)
        script.add_action(INITIALIZE, self.INITIALIZE_DEVICES_ACTION)

    def _add_input_script(self, script: Script):
        """Adds the script to run inputs.

        Args:
            script (Script): an instance of Script
        """

        script.add_action(INPUT, self.HANDLE_MOVE_PREVIEW_ACTION)
        script.add_action(INPUT, self.HANDLE_MOUSE_CLICK_ACTION)
        script.add_action(INPUT, self.HANDLE_NETWORK_MOUSE_CLICK_ACTION)


    def _add_update_script(self, script: Script):
        """Adds the script to update the game

        Args:
            script (Script): an instance of Script
        """
        script.clear_actions(UPDATE)
        script.add_action(UPDATE, self.ADD_PEG_ACTION)
        script.add_action(UPDATE, self.ADD_ALL_POSSIBLE_BRIDGES_ACTION)
        script.add_action(UPDATE, self.CHANGE_PLAYER_ACTION)
        script.add_action(UPDATE, self.HANDLE_WIN_ACTION)
        
        
    def _add_output_script(self, script: Script):
        """Adds the script to output

        Args:
            script (Script): an instance of Script
        """
        script.clear_actions(OUTPUT)
        script.add_action(OUTPUT, self.START_DRAWING_ACTION)
        script.add_action(OUTPUT, self.DRAW_BOARD_ACTION)
        script.add_action(OUTPUT, self.DRAW_PEGS_ACTION)
        script.add_action(OUTPUT, self.DRAW_BRIDGES_ACTION)
        script.add_action(OUTPUT, self.END_DRAWING_ACTION)

    def _add_release_script(self, script: Script):
        """Adds the script to realease the devices.

        Args:
            script (Script): an instance of Script
        """
        script.clear_actions(RELEASE)
        script.add_action(RELEASE, self.RELEASE_DEVICES_ACTION)
