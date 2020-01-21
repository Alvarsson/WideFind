from flask import render_template, url_for, Flask
from app.main import main_bp as bp
import requests

@bp.route('/')
def index():
	return 'Detta är startsidan'


@bp.route('/hejsan')
def index2():
	return 'Detta är andra sidan'


