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
job_id = "long-GUID-here"


def job_wait(job_id):
	print "In the meantime, I will sing you a song..."
	print "........................................................................."
	song = ['Have I told you lately that I love you?', 'Have I told you there\'s no one else above you?', 'Fill my heart with gladness, take away all my sadness', 'Ease my troubles, that\'s what you do', \
	'For the morning sun in all it\'s glory', 'Meets the day with hope and comfort too', 'You fill my life with laughter, somehow you make it better', 'Ease my troubles, that\'s what you do',
	'There\'s a love less defined', 'And its yours and its mine', 'Like the sun', 'And at the end of the day', 'We should give thanks and pray', 'To the one, to the one', \
	'Have I told you lately that I love you?', 'Have I told you there\'s no one else above you?', 'Fill my heart with gladness, take away all my sadness', 'Ease my troubles, that\'s what you do']

    base_url = 'http://%s:8888/api/v2/lcm/' % server_ip
	job_url = "jobs/%s" % job_id

    i = 0
	while i < 40:
		job_response = requests.get(base_url + job_url)
		job_results = json.loads(job_response.text)
		job_status = job_results.get('status')
		if i <= 16:
		    print song[i]
		if job_status == 'COMPLETE':
			print "Alright! The song is over..."
			break
		elif job_status == 'FAILED':
			print "Oh no, the job failed!"
			sys.exit()
		elif job_status == 'WILL_FAIL':
			print "Oh no, the job failed!"
			sys.exit()
		else:
			time.sleep(30)
		i += 1

job_wait(job_id)
