'''
Module for total_gift_cost function

Author: Luiz Coelho
Date: March 2023
'''

# Run pylint holiday_gifts_fixed.py
# until the result is pylint holiday_gifts_fixed.py

# It is possible to use:
# autopep8 --in-place --aggressive --aggressive holiday_gifts_fixed.py
# to fix some thing automatically

import numpy as np


def compute_total_gift_cost(file_path):
    """
    Read file with gift costs and returns the sum of costs of gifts below 25

    Args:
        file_path: (str) path fot gift costs txt
    Returns:
        total_price: (float) the total cost of all gifs below 25
    """

    with open(file_path, 'r', encoding="utf-8") as file_handler:
        gift_costs = file_handler.read().split('\n')

    gift_costs = np.array(gift_costs).astype(int)  # convert string to int
    total_price = (gift_costs[gift_costs < 25]).sum() * 1.08
    return total_price


if __name__ == '__main__':
    print("Total gifts cost: ", end='')
    print(compute_total_gift_cost('gift_costs.txt'))
