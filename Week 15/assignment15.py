from numpy import random

class Adventurer:
    """
    Insert docstring here later
    """
    max_health = 100

    def __init__(self, name):
        self.name = name
        self.health = random.randint(60,91)

    def intro(self):
        """
        Adventurer introduction.
        Returns a string.
        """
        return "Hello my name is " + self.name + "!"

    def needs_heal(self):
        """
        Checks if adventurer needs healing.
        """
        if self.health < 80:
            print ("I need healing!")
            return True
        else:
            print ("I'm fine!")
            return False

    class Healer(Adventurer):
        """
        Insert docstring here later
        """
        def __init__(self, name, medicine_stock):
            super().__init__(name)
            self.medicine_stock = medicine_stock

        def healer_intro(self):
            """
            Insert docstring here later
            """
            