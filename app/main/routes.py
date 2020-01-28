from flask import render_template, url_for, Flask
from app.main import main_bp as bp
import requests
import json
import os
	
def load_json():
	filename = os.path.join(os.path.dirname(__file__), '../static', 'network.json')
	print(filename)
	with open(filename) as node_graph:
		data = json.load(node_graph)
	return data

@bp.route('/')
def index():
	#node_data = load_json()
	#print("hej")
	#print(node_data)
	return render_template("index.html")


@bp.route('/network')
def index2():
	return render_template('/network.json')


