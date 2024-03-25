#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from flask import Flask, g, request, url_for, Response
import settings
from core import log, env
import models
import views
import task
import os, traceback


def create_app():
    run_env = env.get('RUN_ENV', 'production')
    app_path = os.path.dirname(os.path.abspath(__file__))
    app = Flask(__name__, template_folder='{app_path}/templates'.format(app_path=app_path), static_folder='{app_path}/static'.format(app_path=app_path))
    app.config.from_object(settings.configs[run_env])
    log.init(app)
    models.init(app)
    views.init(app)
    app.add_url_rule('/favicon.ico', '', redirect_to='/static/favicon.ico')
    

    @app.before_request
    def beforeRequest():
        g.env = env
        g.app_path = app_path
        g.root_path = app_path
        app.logger.info(request.url)
        app.logger.info(dict(request.form))

    @app.after_request
    def afterRequest(resp: Response):
        if not resp.is_streamed:
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
celery_app = task.init_celery(app)

if __name__ == '__main__':
    app.run(port=env.get('PORT', env.get('PORT')), host='0.0.0.0')
