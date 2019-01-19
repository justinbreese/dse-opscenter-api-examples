import os
import requests
import json

server_ip = "35.160.153.226"
dc_id = "7d5abd51-c95e-4fe3-9d41-99f6e3137d9d" #put the ID from the output of create-datacenter.py here
node_name = "Node0" #name of the node
private_ip = "54.188.178.216" #private IP address of the node
node_ip = "172.31.41.79" #public IP address of the node

base_url = 'http://%s:8888/api/v2/lcm/' % server_ip
opscenter_session = os.environ.get('opscenter_session', '')

def do_post(url, post_data):
    result = requests.post(base_url + url,
                           data=json.dumps(post_data),
                           headers={'Content-Type': 'application/json', 'opscenter-session': opscenter_session})
    print repr(result.text)
    result_data = json.loads(result.text)
    return result_data

make_node_response = do_post("nodes/",
	        {"name": node_name,
	         "listen-address": private_ip,
	         "native-transport-address": "0.0.0.0",
		     "broadcast-address": node_ip,
	         "native-transport-broadcast-address": node_ip,
	         "ssh-management-address": node_ip,
	         "datacenter-id": dc_id,
	         "rack": "rack1"}
             )
