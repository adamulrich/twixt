import pathlib
from game.casting.color import Color

# -------------------------------------------------------------------------------------------------- 
# GENERAL GAME CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# GAME
GAME_NAME = "Twixt"
FRAME_RATE = 2

# SCREEN
SCREEN_WIDTH = 885
SCREEN_HEIGHT = 950
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = (SCREEN_WIDTH) / 2
SCREEN_SCALE = 35

#GRID 
DIRECTION_LEFT_RIGHT = 0
DIRECTION_UP_DOWN = 1
MIN_X = [0,1]
MAX_X = [23, 22]
MIN_Y = [1,0]
MAX_Y = [22, 23]

# FIELD
FIELD_TOP = 60
FIELD_BOTTOM = 1000
FIELD_LEFT = 0
FIELD_RIGHT = SCREEN_WIDTH

# FONT
FONT_FILE = "assets/fonts/zorque.otf"
FONT_SMALL = 32
FONT_LARGE = 48

# SOUND

# TEXT
ALIGN_CENTER = 0
ALIGN_LEFT = 1
ALIGN_RIGHT = 2

# COLORS
BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
PURPLE = Color(255, 0, 255)
RED = Color(178, 42, 42)
GREY = Color(128,128,128)
LIGHT_SLATE_GREY = Color(119,136,153)
DARK_SLATE_GREY = Color(47,79,79)
LIGHT_RED = Color(166, 89, 89)
LIGHTER_RED = Color(211, 134, 134)
PREVIEW_BLACK = Color(55, 55, 61)

PREVIEW_COLORS = {RED: LIGHT_RED, 
                BLACK: PREVIEW_BLACK}

#SIZE
PEG_RADIUS = 10

# SCENES
NEW_GAME = 0
TRY_AGAIN = 1
IN_PLAY = 2
GAME_OVER = 3

# -------------------------------------------------------------------------------------------------- 
# SCRIPTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# PHASES
INITIALIZE = 0
LOAD = 1
INPUT = 2
UPDATE = 3
OUTPUT = 4
UNLOAD = 5
RELEASE = 6

# -------------------------------------------------------------------------------------------------- 
# CASTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

PLAYERS_GROUP = "players"
HOLES_GROUP = "holes"
STATS_GROUP = "stats"
NEW_PEG_GROUP = "new_peg"
CURRENT_PLAYER_GROUP = "current_player"
PREVIEW_GROUP = "preview"

# HUD
HUD_MARGIN = 15

# DIALOG
DIALOG_GROUP = "dialogs"
ENTER_TO_START = "PRESS ENTER TO START"
PREP_TO_LAUNCH = "PREPARING TO LAUNCH"
WAS_GOOD_GAME = "GAME OVER"


#STATUS
STATUS_GROUP = "status"
RED_PLAYERS_TURN = "Red Players Turn"
BLACK_PLAYERS_TURN = "Black Players Turn"
STATUS_MESSAGE = {DIRECTION_LEFT_RIGHT: RED_PLAYERS_TURN, 
                    DIRECTION_UP_DOWN: BLACK_PLAYERS_TURN
                    }
