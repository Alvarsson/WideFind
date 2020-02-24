from flask import render_template, url_for, Flask
from app.main import main_bp as bp
import requests
import json
import os
import pandas as pd
	
def load_json():
	query = """query {
		
	} """
	return data

@bp.route('/')
def index():
	
	return render_template("testfil.html")


@bp.route('/network')
def index2():
	return render_template('/network.json')


