from flask import Flask, render_template
from .site.routes import site

app = Flask(__name__)

app.register_blueprint(site)

# from config import Config
# from .api.routes import api

# from .authentication.routes import auth

# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from models import db as root_db, login_manager, ma
# from flask_cors import CORS
# from helpers import JSONEncoder

# CORS(app)

# app.register_blueprint(auth)
# app.register_blueprint(api)

# app.json_encoder = JSONEncoder
# app.config.from_object(Config)
# root_db.init_app(app)
# login_manager.init_app(app)
# ma.init_app(app)
# migrate = Migrate(app, root_db)