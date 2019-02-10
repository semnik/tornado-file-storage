#!/usr/bin/env python

import tornado.ioloop
import tornado.web
from tornado.options import define, options, parse_command_line
import os
import logging
from filehandler import filehandler

if __name__ == "__main__":

    define("port", default=8888, type=int)
    define('file_storage_path', type=str, default="storage")
    parse_command_line()
    if not os.path.exists(options.file_storage_path):
        os.mkdir(options.file_storage_path)
    application = tornado.web.Application(
        [

            (r"/", filehandler.FileHandler,
             dict(upload_dir=options.file_storage_path)),
        ]
    )
    application.listen(options.port)
    logging.info("Server running on port %d", options.port)
    tornado.ioloop.IOLoop.current().start()
