import os
import requests
import json
import sys
import time

server_ip = "35.160.153.226"
job_id = "c6390494-68d1-4ccf-b128-1fd5e491e8a0" #put the ID from the output of run-job.py script here

base_url = 'http://%s:8888/api/v2/lcm/' % server_ip

def job_wait(job_id):
	job_url = "jobs/%s" % job_id
	i = 0
	print "Please be patient..."
	while i < 50:
		job_response = requests.get(base_url + job_url)
		job_results = json.loads(job_response.text)
		job_status = job_results.get('status')
		if job_status == 'COMPLETE':
			print "The job has completed!"
			break
		elif job_status == 'FAILED':
			print "Oh no, the job failed!"
			sys.exit()
		elif job_status == 'WILL_FAIL':
			print "Oh no, the job is going to fail!"
			sys.exit()
		else:
			time.sleep(30)
		i += 1

job_wait(job_id)
