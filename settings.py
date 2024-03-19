#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from environs import Env
from core import env


class BaseConfig(object):
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = env.get('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


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
