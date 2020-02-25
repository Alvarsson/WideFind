from flask import render_template, url_for, Flask
from app.main import main_bp as bp
import requests
import json
import os
import pandas as pd
from app.main.functions import *


id = "hejsan"
x = 123
y = 345
z = 678
ip = "0.0.0.1337"
mac = "123.123.123.123"
active = "false"
Test_id = "nod"

data_array = []
@bp.route('/')
def index():
	print("hej")
	nodeInfo = load_gateways()
	json_data = json.loads(nodeInfo)
	json_data = json_data.get("data")
	json_data = json_data.get("Gateway")
	json_data = json_data[0]
	for item in json_data.values():
		data_array.append(item)
	print(data_array)
	print("hej")
	#add_result = add_gateway(x,y,z,active,ip)

	return render_template("testfil.html", data_array=data_array )


@bp.route('/network')
def index2():
	return render_template('/network.json')





