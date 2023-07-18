from constants import *
from game.directing.director import Director
from game.directing.scene_manager import SceneManager
import sys


def main():

    network_status = NETWORK_NONE
    connect_to_ip_address = "localhost"

    if len(sys.argv) > 1:
        arg = sys.argv[1].lower()
    
        if arg == "--server":
            network_status = NETWORK_SERVER

        elif arg == "--client":
            network_status = NETWORK_CLIENT

            try: 
                connect_to_ip_address = sys.argv[2].lower()

            except:
                connect_to_ip_address = "localhost"

            


    director = Director(SceneManager.VIDEO_SERVICE, network_status, connect_to_ip_address)


    director.start_game()
    

if __name__ == "__main__":
    main()
