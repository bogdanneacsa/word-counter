# -*- coding: utf-8 -*-
'''
Main entry script for word frequency counter project.

.. moduleauthor:: Bogdan Neacsa <neacsa_bogdan_valentin@yahoo.com>
'''
import os
import tornado.ioloop
import tornado.web
from tornado.options import define, options

from handlers.word_freq_handler import WordFrequencyHandler

# Define specific configuration parameters accepted by script
define("port", default=8080, help="Run on the given port", type=int)
define("debug", default=True, help="Run in debug mode", type=bool)


class Application(tornado.web.Application):
    """ Main application with specific handlers and settings."""
    
    def __init__(self):
        handlers = [
                    (r"/", WordFrequencyHandler),
                    ]
        
        settings = dict(
                        debug = options.debug,
                        static_path = os.path.join(os.path.dirname(__file__), "static"),
                        template_path = os.path.join(os.path.dirname(__file__), "templates"),
                        )
        tornado.web.Application.__init__(self, handlers, **settings)
        

if __name__ == "__main__":
    # Just parse any command line attributes and start
    tornado.options.parse_command_line()
    application = Application()
    application.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
