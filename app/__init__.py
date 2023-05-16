
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.secret_key = '9@.\xf1\x06\xb4xtK\x0e\xbf\x85\xb0pN\xe5'
    db.init_app(app)
    migrate.init_app(app, db)


    # Import auth at the end
    from app.routes.auth import auth_blueprint as auth_bp
    from app.routes.operation import operation_blueprint as op_bp
    from app.routes.record import record_blueprint as rc_bp
    
    app.register_blueprint(auth_bp, url_prefix='/api')
    app.register_blueprint(op_bp, url_prefix='/api')
    app.register_blueprint(rc_bp, url_prefix='/api')
    
    return app