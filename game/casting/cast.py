from game.casting.player import Player
from game.casting.actor import Actor
import constants

class Cast:
    """A collection of actors.

    The responsibility of a cast is to keep track of a collection of actors. It has methods for 
    adding, removing and getting them by a group name.

    Attributes:
        _actors (dict): A dictionary of actors { key: group_name, value: a list of actors }
        _current_player: name of current player.
    """

    def __init__(self):
        """Constructs a new Actor."""
        self._actors = {}
        self._current_player = None
        
    def add_actor(self, group, actor):
        """Adds an actor to the given group.
        
        Args:
            group: A string containing the name of the group.
            actor: The instance of Actor (or a subclass) to add.
        """
        if group not in self._actors.keys():
            self._actors[group] = []
        self._actors[group].append(actor)

    def clear_actors(self, group):
        """Clears actors from the given group.
        
        Args:
            group: A string containing the name of the group.
        """
        if group in self._actors:
            self._actors[group] = []
    
    def clear_all_actors(self):
        """Clears all actors."""
        for group in self._actors:
            self._actors[group] = []
    
    def get_actors(self, group) -> tuple[list[Actor], list[Player] ]:
        """Gets the actors in the given group.
        
        Args:
            group: A string containing the name of the group.

        Returns:
            A list of Actor instances.
        """
        results = []
        if group in self._actors.keys():
            results = self._actors[group].copy()
        return results
    
    def get_all_actors(self):
        """Gets all of the actors in the cast.
        
        Returns:
            A list of actor instances.
        """
        results = []
        for group in self._actors:
            results.extend(self._actors[group])
        return results

    def get_first_actor(self, group):
        """Gets the first actor in the given group.
        
        Args:
            group: A string containing the name of the group.
            
        Returns:
            An instance of Actor.
        """
        result = None
        if group in self._actors.keys():
            if len(self._actors[group]) >0:
                result = self._actors[group][0]
        return result

    def remove_actor(self, group, actor):
        """Removes an actor from the given group.
        
        Args:
            group: A string containing the name of the group.
            actor: The instance of Actor (or a subclass) to remove.
        """
        if group in self._actors:
            self._actors[group].remove(actor)

    def get_next_player(self) -> Player:
        """ This gets the first player in the list of players that is not the current player.
            It will work for two players, will need updated if there were more.

        Returns:
            Player: _description_
        """
        for player in self.get_actors(constants.PLAYERS_GROUP):
            if player is not self.get_first_actor(constants.CURRENT_PLAYER_GROUP):
                return player

