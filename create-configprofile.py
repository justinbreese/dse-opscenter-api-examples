import os
import requests
import json

server_ip = "18.236.149.183"
base_url = 'http://%s:8888/api/v2/lcm/' % server_ip
opscenter_session = os.environ.get('opscenter_session', '')
cluster_name = "testing123"

def do_post(url, post_data):
    result = requests.post(base_url + url,
                           data=json.dumps(post_data),
                           headers={'Content-Type': 'application/json', 'opscenter-session': opscenter_session})
    print repr(result.text)
    result_data = json.loads(result.text)
    return result_data

cluster_profile_response = do_post("config_profiles/",
	    {"name": cluster_name,
	     "datastax-version": "6.7.0",
		 'json': {'cassandra-yaml' : {
		 			  'num_tokens' : 8,
	                  'client_encryption_options' : { 'enabled' : True },
	                 'server_encryption_options' : { 'internode_encryption' : 'all',
								                      'require_client_auth' : True,
								                      'require_endpoint_verification' : False
	                 								}
					 				},
	             },
	     "comment": 'LCM provisioned as %s' % cluster_name})
