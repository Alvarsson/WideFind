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
TODO: Skicka data mellan jsfunction med JQuery/ajax 

OPT TODO: fixa så att noders ID alltid är så små de kan vara
"""

@bp.route('/', methods=['GET', 'POST'])
def index():
	configured_gateways = get_configured_gateways()
	unconfigured_gateways = get_unconfigured_gateways()

	return render_template("testfil.html", configured_gateways=configured_gateways, unconfigured_gateways=unconfigured_gateways)


@bp.route('/network')
def index2():
	return render_template('/network.json')





