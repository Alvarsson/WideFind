from flask import render_template, url_for, Flask
from app.main import main_bp as bp
import requests
import json
import os
import pandas as pd
from app.main.functions import *

"""
TODO: Fixa nodecount!
TODO: -------Kolla kommentarer i test_template med caps-lock och lös dem.-------
TODO: fixa removefunktion och koppla knappen
TODO: Fixa funktion för att para ihop detekterade gateways med inlagda noder, ny view för det?
TODO: Activity feed, vad ska läggas in där?
TODO: Informationen av noder måste ju få all data korrekt
TODO: I activity field, lägg till nod, nog har tagits bort etc. alla event ska dit.
TODO: Skicka data mellan jsfunction med JQuery/ajax 

OPT TODO: fixa så att noders ID alltid är så små de kan vara
"""


id = "hejsan"
x = 321
y = 543
z = 876
ip = "0.0.0.1338"
mac = "321.3213.321.321"
active = "true"
Test_id = "nod"



@bp.route('/', methods=['GET', 'POST'])
def index():

	# data_array = []
	print("hej")
	data_array = parseToData()
	node_dict = data_array[0]
	id_array = data_array[1]
	print(id_array)
	print(node_dict)
	print("hej")

	# if request.method == 'POST':
	# 	request_id = request.form['id_request']

	return render_template("testfil.html", data_array=node_dict, id_array=id_array )


@bp.route('/network')
def index2():
	return render_template('/network.json')





