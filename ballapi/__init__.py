# config
from flask import Flask
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:zt7FsghsnpCjbB@localhost:5432/ballpy'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from . import models
    models.db.init_app(app)
    migrate = Migrate(app, models.db)

    @app.route('/')
    def hello():
        return "Welcome to Ball API"

    from . import reptiles
    app.register_blueprint(reptiles.bp)

    return app