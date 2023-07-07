from dotenv import load_dotenv
from flask_cors import CORS

# To load environment variables
load_dotenv()
from flask import Flask
from config.extension import db, ma, migrate, socketio, UPLOAD_FOLDER
from src.FindFaceApp.view import FindFaceApi


# Flask App initialize with extensions and run
def create_app():
    # Flask app initialize
    app = Flask(__name__, static_folder='static', template_folder='templates')
    CORS(app, resources={r"/*": {"origins": "*"}})
    app.config.from_pyfile('config/configurations.py')

    # Blueprints
    app.register_blueprint(FindFaceApi, url_prefix='/app')

    # Database connection initialize
    # db.init_app(app)

    # Marshmallow initialize
    # ma.init_app(app)

    # Database migrate initialize
    # migrate.init_app(app, db, render_as_batch=False, compare_type=True)

    # socketio.init_app(app, cors_allowed_origins='*')
    # Return App for run in run.py file
    return app


# Run Application
if __name__ == "__main__":
    create_app().run(debug=True, host='0.0.0.0', port=5002)
