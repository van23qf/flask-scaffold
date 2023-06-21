import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db: SQLAlchemy = SQLAlchemy()
migrate: Migrate = Migrate()

def init(app: Flask) -> None:
    db.init_app(app)
    model_path = os.path.dirname(os.path.abspath(__file__))
    for model_file in os.listdir(model_path):
        if model_file.endswith('.py') and model_file != '__init__.py':
            model_name = model_file.replace('.py', '')
            __import__('models.{model_name}'.format(model_name=model_name))
    migrate.init_app(app, db=db)