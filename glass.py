# -----------------------------------------------------------
# Implementation of the Glass class for overflow problem using python
# email jozsef.la.kepes@gmail.com
# -----------------------------------------------------------


class Glass:
    """Liquid container for water overflow problem with specified weight"""

    def __init__(self, row, glass_number, weight):
        self.row = row
        self.glass_number = glass_number
        self.weight = weight
        self.contents = 0
        self.capacity = 250  # default capacity in milli-litres

    def set_contents(self, input_millilitres):
        """Set millilitre liquid content for glass, without factoring in it's weight"""
        setattr(self, 'contents', input_millilitres)

    def set_weighted_contents(self, input_millilitres):
        """Set millilitre liquid content for glass, taking into account it's weight in the row"""
        setattr(self, 'contents', input_millilitres * self.weight)

    def add_contents(self, input_millilitres):
        """Cumulatively add input millilitres to glass"""
        setattr(self, 'contents', self.contents + input_millilitres)

    def get_weight(self):
        """Return weight of glass"""
        return self.weight

    def get_contents(self):
        """Return weight of glass"""
        return self.contents
