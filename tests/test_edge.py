# -----------------------------------------------------------
# Unit tests for overflow problem utilising pytest
# email jozsef.la.kepes@gmail.com
# -----------------------------------------------------------


import pytest
from problem import Problem


def test_unit():
    """Perform unit tests for water overflow problem"""

    # Test 1: Check for negative input litres

    run_1 = Problem()
    with pytest.raises(ValueError, match='\'-1\' is an invalid positive int value'):
        run_1.pour(-1)

    # Test 2: Check for string input litres

    run_2 = Problem()
    with pytest.raises(ValueError, match='\'a\' is an invalid non integer/float value'):
        run_2.pour('a')

    # Test 3: Check for 0 input litres
    run_3 = Problem()
    run_3.pour(0)
    assert run_3.sum_glass_content() == 0

    # Test 5: Check if Row number exists
    run_1 = Problem()
    run_1.pour(2.4)

    with pytest.raises(ValueError, match='Glass row 10 does not exist. Please choose a row between 0 and 5'):
        run_1.get_glass_content(10, 0)

    # Test 6: Check if Glass number exists
    with pytest.raises(ValueError, match='Glass number 1 does not exist in row 0. Please choose a glass between 0 and 1'):
        run_1.get_glass_content(0, 1)
