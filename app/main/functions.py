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