# -*- coding: utf-8 -*-
'''
This module contains tests for the commons.utils module.

.. moduleauthor:: Bogdan Neacsa <neacsa_bogdan_valentin@yahoo.com>
'''

import unittest
from commons.utils import extract_word_frequencies


class UtilsTest(unittest.TestCase):
    
    def test_extract_word_frequencies_happy(self):
        """
        Test the happy flow, where we pass a sentence and compare the
        result with the one we expect.
        """
        expected = [('bear', 2), ('was', 2), ('papa', 1), ('while', 1), 
                    ('mama', 1), ('home', 1), ('out', 1)]
        input_sentence = "Papa bear was home while mama Bear was out."
        result = extract_word_frequencies(input_sentence)
        self.assertEqual(result, expected, 
                         "Expected %s but got %s" % (expected, result))
        
    def test_extract_word_frequencies_empty(self):
        """
        Test case where empty string is passed as input and expect a
        empty list to be returned.
        """
        result = extract_word_frequencies('')
        self.assertEqual([], result, 
                         "Empty list should be returned for empty string.")
        

def suite():
    """
    Gather all the tests in a test suite.
    """
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(UtilsTest))
    return test_suite
