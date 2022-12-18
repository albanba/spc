
from game.casting.actor import Actor
import constants


# TODO: Implement MoveActorsAction class here! 

# Override the execute(cast, script) method as follows:
# 1) get all the actors from the cast
# 2) loop through the actors
# 3) call the move_next() method on each actor

class MoveActorsAction():

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        self._max_x = constants.MAX_X
        self._max_y = constants.MAX_Y
        
        
    def execute(self, cast, script):
        banner = cast.get_first_actor("banners")
        robot = cast.get_first_actor("robots")
        artifacts = cast.get_actors("artifacts")
        blasts = cast.get_actors("blasts")
       
        for artifact in artifacts:
            artifact.move_next(self._max_x, self._max_y)

        for blast in blasts:
            blast.move_next(self._max_x, self._max_y)  
            
       
        robot.move_next(self._max_x, self._max_y)
       
        
        # for blast in blasts:
        #     for artifact in artifacts:
        #         if blast.get_position().equals(artifact.get_position()):
        #             self._points = self._points + artifact.calculate_points()
        #             cast.remove_actor("artifacts", artifact)
        #             cast.remove_actor("blasts", blast)
            
                
                

            