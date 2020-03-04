from flask import render_template, url_for, Flask
from app.main import main_bp as bp
import requests
import json
import os
import pandas as pd

port = 4000
url = "http://localhost:" + str(port)

# Kolla om ni måste parsa om datan för alla noder samt enskilda till id info
def exportJson():
	data = {}

def parseToData():
	array = []
	nodeInfo = load_gateways()
	json_data = json.loads(nodeInfo)
	#print(json_data)
	json_data = json_data.get("data")
	json_data = json_data.get("Gateway")
	#print(json_data)
	json_data = json_data[0]
	#print(json_data)
	for item in json_data.values():
		array.append(item)
	return array

def load_gateways():
	query = """ query { 
		Gateway {
			uuid
			x
			y
			z
			ip_address
			active
		}
	} """
	return send_query(query)

def get_unconfigured_gateways():
    query = """ query { 
		Unconnected {
			gateway { 
      			uuid
      		}
		}
	} """
    return parse_data(send_query(query))

def parse_data(data):
	gateways_str = data
	gateways_json = json.loads(gateways_str)
	return gateways_json["data"]["Unconnected"][0]["gateway"]

def send_query(query):
	parameters = {"query": query}
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

def add_gateway(x, y, z, ip, active):
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


