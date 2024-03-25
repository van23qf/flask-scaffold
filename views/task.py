#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from flask import (
    Blueprint, g, render_template, current_app
)
from task import example

bp = Blueprint('task', __name__, url_prefix='/task')

@bp.route('/add', methods=['POST', 'GET'])
def index():
    # 立即执行
    # example.example_task.delay(1, 1)
    # 延迟三秒执行
    example.example_task.apply_async((1, 2), countdown=3)
    current_app.logger.info('推送任务')
    return '添加成功'
