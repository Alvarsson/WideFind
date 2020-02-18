from flask import Flask, Blueprint
from config import Config


def create_app(config=Config):
	app = Flask(__name__)
	app.config.from_object(config)

	from app.main import main_bp
	app.register_blueprint(main_bp)

	return app
