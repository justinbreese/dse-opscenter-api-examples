import os
import requests
import json

server_ip = "35.160.153.226"
data_center = "DC1"
cluster_id = "0c4a4d93-b481-43f3-8218-3a586559772d" #put the ID from the output of create-cluster.py script here

base_url = 'http://%s:8888/api/v2/lcm/' % server_ip
opscenter_session = os.environ.get('opscenter_session', '')

def do_post(url, post_data):
    result = requests.post(base_url + url,
                           data=json.dumps(post_data),
                           headers={'Content-Type': 'application/json', 'opscenter-session': opscenter_session})
    print repr(result.text)
    result_data = json.loads(result.text)
    return result_data

make_dc_response = do_post("datacenters/",
	        {"name": data_center,
	         "cluster-id": cluster_id,
	         "solr-enabled": True,
	         "spark-enabled": True,
	         "graph-enabled": True}
			 )
dc_id = make_dc_response['id']

print "\ndc_id: " + dc_id
