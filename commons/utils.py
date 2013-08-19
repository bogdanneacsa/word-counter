# -*- coding: utf-8 -*-
'''
This module contains various utilities functions that are needed
by the handlers layer.

.. moduleauthor:: Bogdan Neacsa <neacsa_bogdan_valentin@yahoo.com>
'''

import re
from collections import defaultdict
from operator import itemgetter


def extract_word_frequencies(input_paragraph):
    """
    Given an input paragraph, count how many times each separate word is used.
    Note that words with different capitalizations are considered equal, so
    for the purpose of this function 'Apples' == 'apples'. Also different 
    numbers will also be considered as words. 
    
    :param input_paragraph: a string containing the input text from which the
        word frequencies need to be extracted.
        
    :returns: a list of two elements-tuples with the form: [(word, freq), ..
        sorted by the freq values
    """
    if not input_paragraph:
        return []
    # First construct a helper dictionary of the form {word : frequency}
    word_frequencies = defaultdict(int)
    for word in re.findall(r'\w+', input_paragraph, re.UNICODE):
        word_frequencies[word.lower()] += 1
    # Now just return a list obtained by sorting the helper dict by values
    return sorted(word_frequencies.items(), key=itemgetter(1), reverse=True)
