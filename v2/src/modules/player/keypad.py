class Keypad:
    """
    Join controllers in to a single interface
    """

    def __init__(self):
        self.i_human:   bool = False # △
        self.i_object:  bool = False # o
        self.attack:    bool = False # ∎
        self.deffese:   bool = False # x

        #   ^
        # < @ >
        #   v
        self.directions: list = (
            float, 
            float, 
            float, 
            float
        )
    
    def input(self):
        """
        Get inputs for
        """
        pass