
from game.casting.actor import Actor
import constants


class MoveActorsAction():
    """
    Moves all the actors in their given directions.
    
    The responsibility of MoveActorsActions is to advance the actors postions.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self, keyboard_service):
        """Constructs a new MoveActorsAction."""
        self._keyboard_service = keyboard_service
        self._max_x = constants.MAX_X
        self._max_y = constants.MAX_Y
        
        
    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        
        robot = cast.get_first_actor("robots")
        artifacts = cast.get_actors("artifacts")
        blasts = cast.get_actors("blasts")
       
        for artifact in artifacts:
            artifact.move_next(self._max_x, self._max_y)

        for blast in blasts:
            blast.move_next(self._max_x, self._max_y)  
            
       
        robot.move_next(self._max_x, self._max_y)
       
        
   
            
                
                

            