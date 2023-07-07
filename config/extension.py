from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_socketio import SocketIO
import datetime
import os

# SQLAlchemy initialize
db = SQLAlchemy()

# Migrate initialize
migrate = Migrate()

# Marshmallow initialize
ma = Marshmallow()

socketio = SocketIO()

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
UPLOAD_FOLDER = ROOT_DIR+"/static/uploads/"
