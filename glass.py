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
        setattr(self, 'contents', input_millilitres)