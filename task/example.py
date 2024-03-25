#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from celery import shared_task
from flask import current_app


@shared_task(ignore_result=True)
def example_task(a: int, b: int) -> int:
    result = a + b
    current_app.logger.info('计算结果：{result}'.format(result=result))
    return result
