import constants
from game.casting.actor import Actor

from game.shared.point import Point 
from game.casting.blast import Blast


class HandleCollisionsAction():
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the cycle collides
    with the the segments of the other cycle and handles game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False
        

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
           
            self._handle_collision(cast)
            self._handle_game_over(cast)

    
    def _handle_collision(self, cast):
        """Sets the game over flag if the cycle collides with the segments of the other cycle.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        artifacts = cast.get_actors("artifacts")
        blasts = cast.get_actors("blasts")
        robot = cast.get_actors("robots")[0]
        banner = cast.get_actors("banners")
        
        for blast in blasts:
            for artifact in artifacts:
                if blast.get_position(self).equals(artifact.get_position()):
                    self._points = self._points + artifact.calculate_points()
                    cast.remove_actor("artifacts", artifact)
                    cast.remove_actor("blasts", blast)
                    banner.set_text(f'Score: {self._points}')

        for artifact in artifacts:
            if artifact.get_position().equals(robot.get_position()):
                self._is_game_over = True         
      
        
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the cycles white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            artifacts = cast.get_actors("artifacts")
            
            for artifact in artifacts:
                artifact.set_color(constants.WHITE)

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over!")
            message.set_position(position)
            cast.add_actor("messages", message)

          

          
            