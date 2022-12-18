from game.casting.actor import Actor

class Artifact(Actor):
    """A message represented by a random character with random colors in random positions.  
    
    The Artifact while using Actor inherited methods sets color, positions, text, font size and messages for the artifact.
    Attributes:
        Actor: For setting color, positions, text, and font size for the artifact.
    """
    def __init__(self):
        """Constructs a new Artifact with a new Actor in it using the "super" call and creates the _message variable. 
        """
        super().__init__()
      
    
    def calculate_points(self):

        """determines the points based on the text that it receives  
        """

        points = 0

        if (self.get_text() == '*'):
            points = 1
        
        else:
            points = -1
        
        return points