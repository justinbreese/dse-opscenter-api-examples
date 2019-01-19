import os
import requests
import json

server_ip = "35.160.153.226"
cluster_name = "Test Cluster"
repository_id = "4a25575e-b007-4ba0-8542-722886916f43" #put the ID from the output of create-repo.py script here
machine_credential_id = "db0d3969-487d-4301-b58a-e4711153a807" #put the ID from output of create-credentials.py script here
cassandra_default_password = "Set a password here"
cluster_profile_id = "1200671a-bbe1-470d-9b6e-568017b8fb29" #put the ID from output of create-config_profile.py script here

base_url = 'http://%s:8888/api/v2/lcm/' % server_ip
opscenter_session = os.environ.get('opscenter_session', '')

def do_post(url, post_data):
    result = requests.post(base_url + url,
                           data=json.dumps(post_data),
                           headers={'Content-Type': 'application/json', 'opscenter-session': opscenter_session})
    print repr(result.text)
    result_data = json.loads(result.text)
    return result_data

make_cluster_response = do_post("clusters/",
    {"name": cluster_name,
     "repository-id": repository_id,
     "machine-credential-id": machine_credential_id,
     "old-password": "cassandra",
     "new-password": cassandra_default_password,
     "config-profile-id": cluster_profile_id}
     )
cluster_id = make_cluster_response['id']

print "\ncluster_id: " +cluster_id
