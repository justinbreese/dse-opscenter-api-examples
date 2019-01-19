import os
import requests
import json

server_ip = "35.160.153.226"
creds_name = "Justin Credentials"
username = "ubuntu"
privateKey = "paste your SSH private key here"

base_url = 'http://%s:8888/api/v2/lcm/' % server_ip
opscenter_session = os.environ.get('opscenter_session', '')

def do_post(url, post_data):
    result = requests.post(base_url + url,
                           data=json.dumps(post_data),
                           headers={'Content-Type': 'application/json', 'opscenter-session': opscenter_session})
    print repr(result.text)
    result_data = json.loads(result.text)
    return result_data

machine_credential_response = do_post("machine_credentials/",
     {"name": creds_name,
      "login-user": username,
      "become-mode": "sudo",
      "ssh-private-key": privateKey,
	  "use-ssh-keys": True
    }
)
machine_credential_id = machine_credential_response['id']

print "\nmachine_credential_id: " + machine_credential_id
