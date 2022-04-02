# -----------------------------------------------------------
# Unit tests for overflow problem utilising pytest
# email jozsef.la.kepes@gmail.com
# -----------------------------------------------------------


from problem import Problem


def test_unit():
    """Perform unit tests for water overflow problem"""

    # Test 1: Use 2.4 litres as an input
    run_1 = Problem()
    run_1.pour(2.4)

    # Test 2.4L input for all final glass volumes
    assert run_1.get_glass_content(0, 0) == 250
    assert run_1.get_glass_content(1, 0) == 250
    assert run_1.get_glass_content(1, 1) == 250
    assert run_1.get_glass_content(2, 0) == 250
    assert run_1.get_glass_content(2, 1) == 250
    assert run_1.get_glass_content(2, 2) == 250
    assert run_1.get_glass_content(3, 0) == 112.5
    assert run_1.get_glass_content(3, 1) == 250
    assert run_1.get_glass_content(3, 2) == 250
    assert run_1.get_glass_content(3, 3) == 112.5
    assert run_1.get_glass_content(4, 0) == 0
    assert run_1.get_glass_content(4, 1) == 43.75
    assert run_1.get_glass_content(4, 2) == 87.5
    assert run_1.get_glass_content(4, 3) == 43.75
    assert run_1.get_glass_content(4, 4) == 0

    # Test final total glass volume is the same is the input volume
    assert run_1.sum_glass_content() == 2.4

    # Test 2: Use 15 litres as an input

    run_2 = Problem()
    run_2.pour(15)
    assert run_2.sum_glass_content() == 15

    # Test 3: Use a float as an input

    run_3 = Problem()
    run_3.pour(15.01)
    assert run_3.sum_glass_content() == 15.01
