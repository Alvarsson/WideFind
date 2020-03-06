from flask import render_template, url_for, Flask
from app.main import main_bp as bp
import requests
import json
import os
import pandas as pd

port = 4000
url = "http://localhost:" + str(port)

def get_configured_gateways():
	query = """ {
		Connected {
			gateway {
				uuid
				x
				y
				z
				ip_address
				active
			}
		}
	} """
	gateways_str = send_query(query)
	gateways_json = json.loads(gateways_str)
	print(gateways_json)
	if (gateways_json["data"]["Connected"]):
		return gateways_json["data"]["Connected"][0]["gateway"]
	else:
		return []


def get_unconfigured_gateways():
	query = """ { 
		Unconnected {
			gateway {
				uuid
				x
				y
				z
				ip_address
				active
			}
		}
	} """
	gateways_str = send_query(query)
	gateways_json = json.loads(gateways_str)
	return gateways_json["data"]["Unconnected"][0]["gateway"]

def send_query(query):
	parameters = {"query": query}
	result = requests.post(url, json=parameters)
	return result.text

def delete_gateway(uuid):
	mutation = """ mutation { DeleteGateway(uuid: "%s") {
			id
		}
	}""" % (id)
	parameters = {"query": mutation}
	result = requests.post(url, json=parameters)
	return result.text

def add_gateway(x, y, z, ip, active):
	mutation = """ mutation { CreateGateway(x: %d, y: %d, z: %d, ip_address: "%s", active: %s) {
			uuid
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


def add_connection(fromID, toID):
	mutation = """mutation {AddGatewayNeighbors(from: {id: %d}, to: {id: %d}) {
		from {id}
    	to {id}
  		}
	}""" %(fromID,toID)
	parameters = {"query": mutation}
	result = requests.post(url, json=parameters)
	return result.text


def delete_connection(fromID, toID):
	mutation = """mutation {RemoveGatewayNeighbors(from: {id: %d}, 
                      to: {id: %d}) {
    	from {id}
    	to {id}
		}
	}"""%(fromID, toID)
	parameters = {"query": mutation}
	result = requests.post(url, json=parameters)
	return result.text
	
def update_gateway(id,x,y,z,ip,comment):
    mutation = """ mutation { UpdateGateway(id: %s, x: %d, y: %d, z: %d, ip_address "%s", comment: "%s") {
        id
        x
        y
        z
        ip_address
        active
        comment
        }
    } """ % (id,x,y,z,ip,comment)
