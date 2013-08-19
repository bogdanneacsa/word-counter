# -*- coding: utf-8 -*-
'''
A handler for counting word frequencies for a given input text.

.. moduleauthor:: Bogdan Neacsa <neacsa_bogdan_valentin@yahoo.com>
'''
import tornado.web
from tornado.escape import json_encode

from commons.utils import extract_word_frequencies


class WordFrequencyHandler(tornado.web.RequestHandler):
    
    def get(self):
        """ 
        Just render the simple template since we don't need any arguments
        """
        self.render("index.html")
        
    def post(self):
        """
        Get the input text and return a json of a list with 2-element tuples
        in the form [(word, frequency) ..] ordered by frequency.
        """
        input_text = self.get_argument('input_text', '')
        self.write(json_encode(extract_word_frequencies(input_text)))
