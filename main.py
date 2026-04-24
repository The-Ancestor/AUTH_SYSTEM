from flask import Flask
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from db.database import db
from utils.security import limiter
from config import Config
from routes.auth import auth_bp


jwt = JWTManager()
migrate = Migrate()


def create_app(config_class=Config):
    app = Flask(__name__)
    
    app.config.from_object(config_class)

    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)
    limiter.init_app(app) # Bug fixed!

    app.register_blueprint(auth_bp, url_prefix="/auth")

    return app


if __name__ == "__main__":
    app = create_app()
    with app.app_context() :
         db.create_all()

    app.run(host="0.0.0.0", debug=True)
