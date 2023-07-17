from constants import *
from game.directing.director import Director
from game.directing.scene_manager import SceneManager
import sys


def main():

    network_status = NETWORK_NONE

    if sys.argv.count >1:
        arg = sys.argv[1].lower()
    
        if arg == "server":
            network_status == NETWORK_SERVER

        elif arg == "client":
            network_status == NETWORK_CLIENT


    director = Director(SceneManager.VIDEO_SERVICE, network_status)


    director.start_game()
    

if __name__ == "__main__":
    main()