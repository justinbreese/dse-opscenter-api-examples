import os
import requests
import json

server_ip = "35.160.153.226"
cluster_name = "jbreese-yup"

base_api_url = 'http://'+server_ip+':8888/'
opscenter_session = os.environ.get('opscenter_session', '')

def update_nodesync(url, cluster_name, post_data):
    result = requests.post(base_api_url + cluster_name + url,
                           data=json.dumps(post_data),
                           headers={'Content-Type': 'application/json', 'opscenter-session': opscenter_session})
    print repr(result.text)
    result_data = json.loads(result.text)
    return result_data

update_nodesync("/nodesync", cluster_name,
                    {
                      'enable': ['dse_analytics.*', 'dse_leases.*', 'dse_perf.*', 'OpsCenter.*', 'solr_admin.*']
                    }
)
