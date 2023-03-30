'''
Pytest file to test function days_until_launch()

Author: Luiz Coelho
Date: March 2023
'''

from compute_launch_fixed import days_until_launch

def test_days_until_launch_4():
    """"Test case 1
    """
    assert days_until_launch(22, 26) == 4

def test_days_until_launch_0():
    """"Test case 2
    """
    assert days_until_launch(253, 253) == 0

def test_days_until_launch_0_negative():
    """"Test case 3
    """
    assert days_until_launch(83, 64) == 0

def test_days_until_launch_1():
    """"Test case 4
    """
    assert days_until_launch(9, 10) == 1

def test_days_until_lunch_148():
    """"Test case 5
    """
    assert days_until_launch(123, 271) == 148
