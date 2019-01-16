import os
import requests
import json

server_ip = "18.236.149.183"
cluster_name = "jbreese-yup"
base_api_url = 'http://'+server_ip+':8888/'
opscenter_session = os.environ.get('opscenter_session', '')

def update_keyspace(cluster_name, keyspace, put_data):
    result = requests.put(base_api_url + cluster_name + '/keyspaces/'+keyspace,
                           data=json.dumps(put_data),
                           headers={'Content-Type': 'application/json', 'opscenter-session': opscenter_session})
    print repr(result.text)
    result_data = json.loads(result.text)
    return result_data

print "updating the keyspaces with NetworkTopologyStrategy..."
keyspaces = ['OpsCenter', 'dse_security', 'dse_analytics', 'dse_perf', 'dse_system_local', 'dsefs', 'HiveMetaStore']
for keyspace in keyspaces:
    update_keyspace(cluster_name, keyspace,
        {
        "strategy_class": "org.apache.cassandra.locator.NetworkTopologyStrategy",
        "strategy_options": {"onprem" : "3", "AWS" : "3", "Azure" : "3", "GCP" : "3"},
        "durable_writes": True
        }
    )
