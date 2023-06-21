#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from flask import Flask, g, request
import logging
from logging.handlers import TimedRotatingFileHandler
import settings
import models
#from models.user import User
import views
import os, traceback, json
from environs import Env


def create_app():
    env = Env()
    env.read_env()
    run_env = env.str('RUN_ENV') if env.str('RUN_ENV') else 'production'
    app_path = os.path.dirname(os.path.abspath(__file__))
    app = Flask(__name__, template_folder='{app_path}/templates'.format(app_path=app_path), static_folder='{app_path}/static'.format(app_path=app_path))
    app.config.from_object(settings.configs[run_env])
    models.init(app)
    views.init(app)

    loghandler = TimedRotatingFileHandler('{app_path}/logs/flask.log'.format(app_path=app_path), when="MIDNIGHT", interval=30, backupCount=12, encoding="UTF-8", delay=False, utc=True)
    loghandler.setLevel(logging.DEBUG)
    loggingFormat = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
    loghandler.setFormatter(loggingFormat)
    app.logger.addHandler(loghandler)

    @app.before_request
    def beforeRequest():
        g.env = env
        g.app_path = app_path
        g.root_path = app_path
        app.logger.info(request.url)
        app.logger.info(dict(request.form))

    @app.after_request
    def afterRequest(resp):
        app.logger.info(resp.data.decode("unicode_escape"))
        return resp

    @app.errorhandler(Exception)
    def internalError(e):
        app.logger.error(traceback.format_exc())
        return {'code': 500, 'message': str(e)}

    return app

app = create_app()
db = models.db
migrate = models.migrate

if __name__ == '__main__':
    env = Env()
    env.read_env()
    port = env.str('PORT') if env.str('PORT') else 9000
    app.run(port=port, host='0.0.0.0')
