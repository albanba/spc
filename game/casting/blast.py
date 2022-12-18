import constants
from game.casting.actor import Actor
from game.shared.point import Point
from game.casting.cast import Cast


class Blast(Actor):
    """
    Star Wars phaser look a like 
    
    The responsibility of blast is to move itself.

    Attributes:
        blast = : single character always moving forward until collision.
    """
    def __init__(self, color):
        super().__init__()
        self.set_color(color)
        self._blast= []
        # self._fire_blast()

    # def get_blast(self):
    #     """Gets the Blast's.
        
    #     Returns:
    #         _blast: The blast body.
    #     """
    #     return self._blast

    # def move_next(self):
        # """Moves the blast forward to the top of the screen. 
            
        
        # Args:
        #     move_next(): moves the blast to the new postion
        # """

        
        # for segment in self._segments:
        #     segment.move_next()
        # # update velocities
        # for i in range(len(self._segments) - 1, 0, -1):
        #     trailing = self._segments[i]
        #     previous = self._segments[i - 1]
        #     velocity = previous.get_velocity()
        #     trailing.set_velocity(velocity)

    # def get_head(self):
    #     """Gets the first segmen of the cycle.
        
    #     Returns:
    #         segment: The actor's position, velocity, text and color.
    #     """
    #     return self._segments[0]

    # def grow_tail(self, number_of_segments, color):

    #     """Grows the actor's tail.
        
    #     Returns:
    #         segment: new segment appended to the cycle's body.
    #     """
        
    #     for i in range(number_of_segments):
    #         tail = self._segments[-1]
    #         velocity = tail.get_velocity()
    #         offset = velocity.reverse()
    #         position = tail.get_position().add(offset)
            
    #         segment = Actor()
    #         segment.set_position(position)
    #         segment.set_velocity(velocity)
    #         segment.set_text("#")
    #         segment.set_color(color)
    #         self._segments.append(segment)

    # def turn_head(self, velocity):
    #     """turns the actor's first segment.
        
    #     Args:
    #         set_velocity(velocity)
    #     Returns:
    #         _segments[0]: The actor's first segment with a new velocity.
    #     """
    #     self._segments[0].set_velocity(velocity)
    
    # def _fire_blast(self):
    #     """Fires the initial body of the blast with their own color.
        
    #         Args:
    #         Point class
    #         and several methods from the Actor class.  
    #     """
    #     x = 0.0
    #     y = 0.0
        
    #     robot = cast.get_actors("robots")
    #     robot_position = robot.get_position()

    #     for i in range(constants.CYCLE_LENGTH):
    #         position = Point(x - i * constants.CELL_SIZE, y)
    #         velocity = Point(1 * constants.CELL_SIZE, 0)
    #         text = "8" if i == 0 else "#"
    #         #color = constants.YELLOW if i == 0 else constants.GREEN
            
    #         segment = Actor()
    #         segment.set_position(position)
    #         segment.set_velocity(velocity)
    #         segment.set_text(text)
    #         segment.set_color(self.get_color())
    #         self._segments.append(segment)