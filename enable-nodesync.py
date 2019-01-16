import os
import sys
import requests
import json
import threading
import argparse
import subprocess
import webbrowser
import time

server_ip = "54.202.212.179"
cluster_name = "jbreese-killrvideo"
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
                      'enable': ['dse_analytics.*', 'dse_leases.*', 'dse_perf.*', 'dse_security.*', 'dse_system.*', 'dse_system_local.*', 'dsefs.*', 'HiveMetaStore.*', 'OpsCenter.*', 'solr_admin.*', 'system_auth.*', 'system_distributed.*', 'system_traces.*']
                    }
)
