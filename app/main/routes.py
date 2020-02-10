from flask import render_template, url_for, Flask
from app.main import main_bp as bp
import requests
import json
import networkx as nx
from networkx.readwrite import json_graph
import matplotlib.pyplot as plt
import os
	
def load_json():
	filename = os.path.join(os.path.dirname(__file__), '../static', 'network.json')
	print(filename)
	with open(filename) as node_graph:
		data = json.load(node_graph)
	return data

@bp.route('/')
def index():

	return render_template("testfil.html")


@bp.route('/network')
def index2():
	return render_template('/network.json')


