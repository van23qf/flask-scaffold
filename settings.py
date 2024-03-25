#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from environs import Env
from core import env


class BaseConfig(object):
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = env.get('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CELERY=dict(
        broker_url='redis://{host}:{port}/{database}'.format(host=env.get('REDIS_HOST'), port=env.get('REDIS_PORT'), database=env.get('REDIS_DB')),
        result_backend='redis://{host}:{port}/{database}'.format(host=env.get('REDIS_HOST'), port=env.get('REDIS_PORT'), database=env.get('REDIS_DB')),
        task_ignore_result=True,
        queues={
                'default': {
                'exchange': 'default',
                'binding_key': 'task.default',
            }
        }
    )

class ProductionConfig(BaseConfig):
    TESTING = False
    DEBUG = False


class DevelopConfig(BaseConfig):
    TESTING = True
    DEBUG = True


configs = {
    # 生产环境
    'production': ProductionConfig,
    # 测试环境
    'development': DevelopConfig
}
