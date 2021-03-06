import os

from flask import Flask

def create_app(test_config=None):
    # creation and configuration of the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'db.sqlite')
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    # make sure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import fizzbuzz
    app.register_blueprint(fizzbuzz.bp)
    
    return app

app = create_app()