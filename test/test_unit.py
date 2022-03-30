# -----------------------------------------------------------
# Unit tests for overflow problem utilising pytest
# email jozsef.la.kepes@gmail.com
# -----------------------------------------------------------


import overflow

import pytest

def unit_test_flow():
     """Perform unit tests for water overflow problem"""

     input_litres = 1.5
     row = 1
     glass = 1
     assert calculate(input_litres, row, glass) == 1
     assert calculate(input_litres, row, glass) == 2
     assert calculate(input_litres, row, glass) == 3
     assert calculate(input_litres, row, glass) == 4
     assert calculate(input_litres, row, glass) == 5