import constants
from game.scripting.action import Action
from game.shared.point import Point
from game.casting.blast import Blast


class ControlActorsAction(Action):
    """
    An input action that controls the Blast.
    
    The responsibility of ControlActorsAction is to get the direction and move the blasts ahead.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service, cast):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self.robot = cast.get_first_actor("robots")
        self.blasts = []
        self._direction = Point(constants.CELL_SIZE, 0)
        

    def execute(self, cast, _keyboard_service):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        velocity = self._keyboard_service.get_direction()
        self.robot.set_velocity(velocity)  
        
        # blasts = cast.get_actors("blasts")

        # for i in blasts:
        #     self._direction = Point(0,-1).scale(self._cell_size)
        
        create = self._keyboard_service.create_blast()
        if create == True: 

            # create blast
            
            blast = Blast(constants.YELLOW)
            blast.set_position(self.robot.get_position())
            blast.set_velocity(Point(0, -1))
            blast.set_text("|")
            blast.set_font_size(constants.FONT_SIZE)
            blast.set_color(constants.YELLOW)
            cast.add_actor("blasts", blast) 

