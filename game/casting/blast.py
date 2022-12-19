import constants
from game.casting.actor import Actor



class Blast(Actor):
    """
    Star Wars phaser look a like 
    
    The responsibility of blast is to create a new instance of itself.

    Attributes:
        blast = : single character always moving forward until collision.
    """
    def __init__(self, color):
        super().__init__()
        self.set_color(color)
        self._blast= []
      