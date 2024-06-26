#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from flask import Flask, render_template
from views import user, index, task


def init(app: Flask) -> None:
    app.register_blueprint(index.bp)
    app.register_blueprint(user.bp)
    app.register_blueprint(task.bp)
