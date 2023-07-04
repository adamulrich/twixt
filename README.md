# cse210-final - Twi

# Team
* Abel Aguilar
* Adam Ulrich
* Andre Silva

# game definition
Twixt is played on a board comprising a 24×24 square grid of holes (minus 4 corner holes). The game has two types of playing pieces, pegs, which fit into the holes, and links, which fit into the top of the peg pieces and are used to connect to peg pieces. In the 3M edition, players are Red and Black; different sets may use different colors. The topmost and bottommost rows of holes belong to the lighter color; the leftmost and rightmost rows to the darker color.

# game rules
The players take turns placing pegs of their respective colors on the board, one peg per turn.
The player with the lighter color makes the first move.
A player may not place a peg on their opponent's border rows.
After placing a peg, a player may link one or more pairs of pegs on the board of their color. The links can only connect two pegs a knight's move away from each other, and cannot cross another link; they block other links, most importantly those of the opponent. As part of the player's move, they may remove their own links (but not those of the opponent) in order to rearrange the sequence of links on the board.
The object is to make a continuous chain of linked pegs connecting the player's border rows. If neither player can achieve this, the game is a draw.

# Minimum viable product 

* Allowing each player to place peg
* Automatic placement of all possible bridges
* Determining if a win happened.
* Basic graphics for board and pegs
* All moves must be validated and legal

# Stretch goals

* Better graphics
* Removal of bridges or allowing a player to cross their own bridge.

# Design details

* We decided to use the batter code base as our initial source for the game, leveraging that structure. We will throw out all the actions. We also need to implement a player class and peg class that inherits from actor.

* There are two computational challenges in the game. One is handling placement of links. Is there a link already in the way. The second is to handle whether a player has one, walking the links from one side of the board to the other.

1. For the first problem, we found this helpful tutorial on how to calculate https://algorithmtutor.com/Computational-Geometry/Check-if-two-line-segment-intersect/Links to an external site.

2. For the second problem, we discussed different data structures, such as a tree. However, with twixt, you can have cycles, which won’t work with a tree. So we opted for a graph, and a graph in python can be represented as a list of nodes as keys in a dictionary, with a list of the node connections as the values, like this:

graph = {(12,12): [(11,10)],
         (11,10): [(12,12), (10,8), (12,8)],
         (12,8): [(11,10)],
         (10,8): [(11,10), (8,7)]
         (8,7): [(10,8)]
}

With a graph, we can use a walking function to determine if there is a path from the 0/1 to 22/23 in the x or y directions by getting all the nodes that have a 0/1 x/y and 22/23 x/y, then do a nested loop walking all possible begin and end points. We discussed using the cast object here, but opted have the player maintain the graph as a separate list as the all positions on the board start out as pegs, but they are in an empty group. When the player selects one, it gets moved from empty to 'red' or 'black' group, and the player adds it to it's graph with any links.

We created a UML diagram discussing the new classes we would need, and followed the scene manager model for breaking these tasks up.

# maintenance
We will work towards our MVP goals, and then should be able to add the stretch goals without needing to make any design changes to the code; incremental changes without redesign is a big part of maintenance. We will also discuss any interface changes in slack so that we are all on the same page.
