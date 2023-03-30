'''
Solution for logging_exercise.py

Author: Luiz Coelho
Date: March 2023
'''


## STEPS TO COMPLETE ##
# 1. import logging
# 2. set up config file for logging called `results.log`
# 3. add try except with logging for success or error
#    in relation to checking the types of a and b
# 4. check to see that log is created and populated correctly
#    should have error for first function and success for
#    the second
# 5. use pylint and autopep8 to make changes
#    and receive 10/10 pep8 score


import logging

logging.basicConfig(
    filename='./results.log',
    level=logging.INFO,
    filemode='w',
    format='%(name)s - %(levelname)s - %(message)s')

def sum_vals(value_a, value_b):
    '''
    Args:
        value_a: (int)
        value_b: (int)
    Return:
        value_a + value_b (int)
    '''
    try:
        assert isinstance(value_a, int)
        assert isinstance(value_b, int)
        result = value_a+value_b
        logging.info("Sum was successful")
        return result
    except AssertionError:
        logging.error("Arguments must be int")
        return None


if __name__ == "__main__":
    sum_vals('no', 'way')
    sum_vals(4, 5)
