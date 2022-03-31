# -----------------------------------------------------------
# Unit tests for overflow problem utilising pytest
# email jozsef.la.kepes@gmail.com
# -----------------------------------------------------------


import overflow

import pytest

def unit_test_flow():
     """Perform unit tests for water overflow problem"""

     # calculate(input_litres, row, glass) == result
     assert calculate(0, 1, 2) == 0

     assert calculate(0.1, 1, 1) == 0.1

     assert calculate(1, 4, 2) == 

     assert calculate(2.5, 6, 7) == 

     assert calculate(20, 6, 7) == 

     assert calculate(100, 6, 7) == 