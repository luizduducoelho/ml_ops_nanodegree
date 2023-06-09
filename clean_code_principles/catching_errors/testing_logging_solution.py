'''
Solution for testing_logging.py

Author: Luiz Coelho
Date: March 2023
'''

## STEPS TO COMPLETE ##
# 1. import logging
# 2. set up config file for logging called `test_results.log`
# 3. add try except with logging and assert tests for each function
#    - consider denominator not zero (divide_vals)
#    - consider that values must be floats (divide_vals)
#    - consider text must be string (num_words)
# 4. check to see that the log is created and populated correctly
#    should have error for first function and success for
#    the second
# 5. use pylint and autopep8 to make changes
#    and receive 10/10 pep8 score

import logging

logging.basicConfig(
    filename='./test_results.log',
    level=logging.INFO,
    filemode='w',
    format='%(name)s - %(levelname)s - %(message)s')


def divide_vals(numerator, denominator):
    '''
    Args:
        numerator: (float) numerator of fraction
        denominator: (float) denominator of fraction

    Returns:
        fraction_val: (float) numerator/denominator
    '''
    try:
        assert isinstance(numerator, float)
        assert isinstance(numerator, float)
        fraction_val = numerator/denominator
        logging.info("Division: SUCCESS")
        return fraction_val
    except ZeroDivisionError:
        logging.error("Denominator can not be zero")
        return None
    except AssertionError:
        logging.error("Arguments must be float")
        return None


def count_words(text):
    '''
    Args:
        text: (string) string of words

    Returns:
        num_words: (int) number of words in the string
    '''
    try:
        assert isinstance(text, str)
        num_words = len(text.split())
        logging.info("Word counting: SUCCESS")
        return num_words
    except AssertionError:
        logging.error("Text argument must be a string")
        return None

if __name__ == "__main__":
    divide_vals(3.4, 0)
    divide_vals(4.5, 2.7)
    divide_vals(-3.8, 2.1)
    divide_vals(1, 2)
    count_words(5)
    count_words('This is the best string')
    count_words('one')
    