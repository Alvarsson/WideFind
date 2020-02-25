from flask import render_template, url_for, Flask
from app.main import main_bp as bp
import requests
import json
import os
import pandas as pd

port = 4000
url = "http://127.0.0.1:" + str(port)

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

def delete_gateway(id):
	mutation = """ mutation { DeleteGateway(id: "%s") {
			id
		}
	}""" % (id)
	parameters = {"query": mutation}
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

