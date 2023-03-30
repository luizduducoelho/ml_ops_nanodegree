'''
Solution for try except clauses

Author: Luiz Coelho
Date: March 2023
'''

def divide_vals(numerator, denominator):
    '''
    Args:
        numerator: (float) numerator of fraction
        denominator: (float) denominator of fraction

    Returns:
        fraction_val: (float) numerator/denominator
    '''
    # try to return the fraction but if the denominator is zero
    # catch the error and return a string saying:
    # "denominator cannot be zero"
    try:
        return numerator/denominator
    except ZeroDivisionError:
        return "Can not perform division by zero."


def num_words(text):
    '''
    Args:
        text: (string) string of words

    Returns:
        num_words: (int) number of words in the string
    '''
    # try to split based on spaces and return num of words
    # but if text isnt a string return "text argument must be a string"
    try:
        return len(text.split(' '))
    except AttributeError:
        return "Text argument must be a string"

if __name__ == '__main__':

    print(divide_vals(1, 2))
    print(divide_vals(1, 0))

    print(num_words("I went to the store yesterday"))
    print(num_words(3))
