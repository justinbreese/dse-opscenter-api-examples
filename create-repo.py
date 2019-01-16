import os
import requests
import json

server_ip = "18.236.149.183"
base_url = 'http://%s:8888/api/v2/lcm/' % server_ip
opscenter_session = os.environ.get('opscenter_session', '')

def do_post(url, post_data):
    result = requests.post(base_url + url,
                           data=json.dumps(post_data),
                           headers={'Content-Type': 'application/json', 'opscenter-session': opscenter_session})
    print repr(result.text)
    result_data = json.loads(result.text)
    return result_data

# setup the repository for where you want to download DSE from
repository_response = do_post("repositories/",
    {"name": "AcmeCo Repo",
        "username": "foo",
        "password": "bar",})

# get the id of the repo that you just created, if you want to...
repository_id = repository_response['id']
