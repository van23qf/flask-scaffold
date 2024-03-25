#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from flask import (
    Blueprint, g, render_template, current_app
)

bp = Blueprint('index', __name__)

@bp.route('/', methods=['GET', 'POST'])
def index():
    return 'hello world'