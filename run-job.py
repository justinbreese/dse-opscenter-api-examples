import os
import requests
import json

server_ip = "18.236.149.183"
base_url = 'http://%s:8888/api/v2/lcm/' % server_ip
opscenter_session = os.environ.get('opscenter_session', '')
cluster_name = "jbreese-yup"
resource_id = "7ee8c523-5395-4ad3-a091-3031045165ec"

def do_post(url, post_data):
    result = requests.post(base_url + url,
                           data=json.dumps(post_data),
                           headers={'Content-Type': 'application/json', 'opscenter-session': opscenter_session})
    print repr(result.text)
    result_data = json.loads(result.text)
    return result_data

install_job = do_post("actions/install",
	                     {"job-type":"install",
	                      "job-scope":"cluster",
	                      "resource-id": resource_id,
						  "concurrency-strategy": "cluster-at-a-time",
	                      "continue-on-error":"false"})
