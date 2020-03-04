from flask import render_template, url_for, Flask
from app.main import main_bp as bp
import requests
import json
import os
import pandas as pd

port = 4000
url = "http://127.0.0.1:" + str(port)

# Kolla om ni måste parsa om datan för alla noder samt enskilda till id info
def exportJson():
    data = load_gateways() #Get data as json
    data = json.loads(data) #parse to string form without newrow slashes
    with open('json_data.txt', 'w') as node_json:
        json.dump(data, node_json)

def parseToData():
    temp_array = []
    id_array = []
    nodeInfo = load_gateways()
    json_data = json.loads(nodeInfo)
    json_data = json_data.get("data")
    json_data = json_data.get("Gateway")
    node_data = []
    for i in json_data:
        node_data.append(i) 
    print(node_data)
    for nodes in json_data:
        for item in nodes.values():
            temp_array.append(item)
    print("HHHHHHHHHHH")
    print(temp_array)
    for id in temp_array[::6]:
        id_array.append(id) #Get array of id's
    return node_data, id_array

def load_gateways():
	query = """ query { Gateway {
			id
			x
			y
			z
			ip_address
			active
		}
	} """
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

def add_gateway( x, y, z, ip, active):
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


