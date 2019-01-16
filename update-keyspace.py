import os
import sys
import requests
import json
import threading
import argparse
import subprocess
import webbrowser
import time

server_ip = "35.167.133.146"
cluster_name = "jbreese-killrvideo"
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
keyspaces = ['killrvideo','killrvideo_sample_data', 'killrvideo_video_recommendations', 'killrvideo_video_recommendations_system', 'killrvideo_web', 'system_auth', 'system_traces', 'dse_leases', 'OpsCenter', 'dse_security', 'dse_analytics', 'dse_perf', 'dse_system_local', 'dsefs', 'HiveMetaStore']
for keyspace in keyspaces:
    update_keyspace(cluster_name, keyspace,
        {
        "strategy_class": "org.apache.cassandra.locator.NetworkTopologyStrategy",
        "strategy_options": {"onprem" : "3", "AWS" : "3", "Azure" : "3", "GCP" : "3"},
        "durable_writes": True
        }
    )
