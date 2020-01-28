from decouple import config
from dotenv import load_dotenv
from flask import Flask, render_template
from .models import DB, User

load_dotenv()

def create_app():
    """Create and configure an instance of the Flask application"""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')
    DB.init_app(app)

    @app.route('/')
    def root():
        return render_template('base.html', title='the great Twitter twitoff!', users=User.query.all())

    return app
