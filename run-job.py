import os
import requests
import json

server_ip = "35.160.153.226"
resource_id = "5159ba3a-a4bd-48b4-ac3d-b19376470724" #put the ID from the output of create-cluster.py script here
scope = "cluster"

base_url = 'http://%s:8888/api/v2/lcm/' % server_ip
opscenter_session = os.environ.get('opscenter_session', '')

def do_post(url, post_data):
    result = requests.post(base_url + url,
                           data=json.dumps(post_data),
                           headers={'Content-Type': 'application/json', 'opscenter-session': opscenter_session})
    print repr(result.text)
    result_data = json.loads(result.text)
    return result_data

install_job = do_post("actions/install",
	                     {"job-type":"install",
	                      "job-scope":scope,
	                      "resource-id": resource_id,
						  "concurrency-strategy": "cluster-at-a-time",
	                      "continue-on-error":"false"}
                          )
job_id = install_job['id']

print "\njob_id: " +job_id
