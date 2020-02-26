from flask import render_template, url_for, Flask
from app.main import main_bp as bp
import requests
import json
import os
import pandas as pd
from app.main.functions import *

"""
TODO: -------Kolla kommentarer i test_template med caps-lock och lös dem.-------
TODO: fixa removefunktion och koppla knappen
TODO: Fixa funktion för att para ihop detekterade gateways med inlagda noder, ny view för det?
TODO: Activity feed, vad ska läggas in där?
TODO: Informationen av noder måste ju få all data korrekt
TODO: I activity field, lägg till nod, nog har tagits bort etc. alla event ska dit.
"""


id = "hejsan"
x = 321
y = 543
z = 876
ip = "0.0.0.1338"
mac = "321.3213.321.321"
active = "true"
Test_id = "nod"



@bp.route('/')
def index():
	data_array = []
	print("hej")
	#add_gateway(x,y,z,ip,active)
	#JA HÄR KOMMER DU BEHÖVA ÄNDRA NÅGOT OCKSÅ VA?
	data_array = parseToData()
	print(data_array)
	print("hej")

	return render_template("testfil.html", data_array=data_array )


@bp.route('/network')
def index2():
	return render_template('/network.json')





