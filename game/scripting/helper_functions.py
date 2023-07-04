"""These helper functions are used across multiple actions, so pulling them out into a separate file
"""

import constants
from game.scripting.action import Action
from game.casting.cast import Cast
from game.casting.player import Player
from game.casting.point import Point
from game.casting.peg import Peg


def get_potential_bridge_list(cast: Cast, player:Player, new_peg: Peg):
    """ returns a list of pairs of pegs for that represent bridges that could 
        be added if the peg was placed on the board for this player.

    Args:
        cast (Cast): An instance of Cast
        player (Player): An instance of Player
        new_peg (Peg): An instance of Peg

    Returns:
        list(list(peg)) 
    """
    possible_bridges = player.get_possible_new_bridge_list(new_peg)
    create_bridges = []
    current_bridges = []

    for p in cast.get_actors(constants.PLAYERS_GROUP):
        current_bridges += p.get_bridges()

    
    for possible_bridge in possible_bridges:
        add_bridge = True
        for current_bridge in current_bridges:
           
            if _intersects(possible_bridge, current_bridge):
                add_bridge = False
                break
        if add_bridge:
            create_bridges.append(possible_bridge)

    return create_bridges

def _direction(p1: Point, p2: Point, p3: Point):
    """ calculates a direction value for the points provided to determine if 
        a line segment intersects with another line segment.

    Args:
        p1 (Point): An instance of Point
        p2 (Point): An instance of Point
        p3 (Point): An instance of Point

    Returns:
        int
    """
    return _cross_product(p3.subtract(p1), p2.subtract(p1))

def _intersects(bridge1, bridge2):
    """ determine if two line segments intersect

    Args:
        bridge1 (list(Point, Point)): a list containing two points
        bridge2 (list(Point, Point)): a list containing two points

    Returns:
        bool: True/False
    """
    b1_0_x = bridge1[0].get_position().get_x()
    b1_0_y = bridge1[0].get_position().get_y()
    b1_1_x = bridge1[1].get_position().get_x()
    b1_1_y = bridge1[1].get_position().get_y()

    b2_0_x = bridge2[0].get_position().get_x()
    b2_0_y = bridge2[0].get_position().get_y()
    b2_1_x = bridge2[1].get_position().get_x()
    b2_1_y = bridge2[1].get_position().get_y()


    p1 = Point(b1_0_x,b1_0_y)
    p2 = Point(b1_1_x,b1_1_y)
    p3 = Point(b2_0_x,b2_0_y)
    p4 = Point(b2_1_x,b2_1_y)

    d1 = _direction(p3, p4, p1)
    d2 = _direction(p3, p4, p2)
    d3 = _direction(p1, p2, p3)
    d4 = _direction(p1, p2, p4)

    if ((d1 > 0 and d2 < 0) or (d1 < 0 and d2 > 0)) and \
        ((d3 > 0 and d4 < 0) or (d3 < 0 and d4 > 0)):
        return True

def _cross_product(p1, p2):
    """ provides the cross product for two points. Used to determine if two line segments
        intersect

    Args:
        p1 (Point): An instance of Point
        p2 (Point): An instance of Point

    Returns:
        number (float,int): the cross product
    """
    return p1.get_x() * p2.get_y() - p2.get_x() * p1.get_y()

