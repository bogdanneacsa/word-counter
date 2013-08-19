# -*- coding: utf-8 -*-
'''
A simple test runner.

.. moduleauthor:: Bogdan Neacsa <neacsa_bogdan_valentin@yahoo.com>
'''
import unittest
import tests.utils_tests as utils_tests


def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(utils_tests.suite())
    return test_suite


if __name__ == "__main__":
    test_runner = unittest.TextTestRunner()
    test_suite = suite()
    test_runner.run(test_suite)
