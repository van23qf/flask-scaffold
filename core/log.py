#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
from flask import Flask
import logging
from logging.handlers import TimedRotatingFileHandler


def init(app: Flask):
    basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    loghandler = TimedRotatingFileHandler('{basedir}/logs/flask.log'.format(basedir=basedir), when="MIDNIGHT", interval=30, backupCount=12, encoding="UTF-8", delay=False, utc=True)
    loghandler.setLevel(logging.DEBUG)
    logging_format = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
    loghandler.setFormatter(logging_format)
    app.logger.addHandler(loghandler)

if __name__ == '__main__':
    pass
