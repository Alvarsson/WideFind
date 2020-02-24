from flask import render_template, url_for, Flask
from app.main import main_bp as bp
import requests
import json
import os
import pandas as pd
import functions

port = 4000
url = "http://127.0.0.1:" + str(port)

id = "hejsan"
x = 123
y = 345
z = 678
ip = "0.0.0.1337"
mac = "123.123.123.123"
active = "false"
Test_id = "nod"
	
def load_gateways():
	query = """ query { Gateway {
			id
			x
			y
			z
			ip_address
			active
			neighbors {
				_id
			}
		}
	} """
	parameters = {"query": query}
	print(parameters)
	result = requests.post(url, json=parameters)
	return result.text

def add_gateway( x, y, z, active, ip):
	mutation = """ mutation { CreateGateway(x: %d, y: %d, z: %d, ip_address: "%s", active: %s) {
			id
			x
			y
			z
			ip_address
			active
		}
	}""" % (x,y,z,ip,active)
	parameters = {"query": mutation}
	result = requests.post(url, json=parameters)
	return result.text

def delete_gateway(id):
	mutation = """ mutation { DeleteGateway(id: "%s") {
			id
		}
	}""" % (id)
	parameters = {"query": mutation}
	result = requests.post(url, json=parameters)
	return result.text

@bp.route('/')
def index():
	load_result = load_gateways()
	print("hej")
	add_result = add_gateway(x,y,z,active,ip)

	return render_template("testfil.html", load=load_result)


@bp.route('/network')
def index2():
	return render_template('/network.json')





