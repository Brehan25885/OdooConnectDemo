from app import app
from flask import render_template,request  # importing the render_template function

import json
import random
import urllib.request

# defining a route
@app.route("/", methods=['GET', 'POST', 'PUT']) # decorator
def home(): # route handler function
	return render_template('index.html')

HOST = '172.30.0.1'
PORT = 8069
DB = 'test'
USER = 'admin'
PASS = 'admin'

def json_rpc(url, method, params):
	data = {
		"jsonrpc": "2.0",
		"method": method,
		"params": params,
		"id": random.randint(0, 1000000000),
	}
	req = urllib.request.Request(url=url, data=json.dumps(data).encode(), headers={
		"Content-Type":"application/json",
	})
	reply = json.loads(urllib.request.urlopen(req).read().decode('UTF-8'))
	if reply.get("error"):
		raise Exception(reply["error"])
	return reply["result"]

def call(url, service, method, *args):
	return json_rpc(url, "call", {"service": service, "method": method, "args": args})



@app.route('/form-handler', methods=['POST'])
def handle_data():
	print('inside hander')
	url = "http://%s:%s/jsonrpc" % (HOST, PORT)
	uid = call(url, "common", "login", DB, USER, PASS)

	# create a new note
	args = {
		'name': request.form['name'],
		'customer_rank':11,
		'phone':request.form['contact']
	}
	res_partner = call(url, "object", "execute", DB, uid, PASS, 'res.partner', 'create', args)
	return "Request received successfully!"

