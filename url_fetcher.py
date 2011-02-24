#! /usr/bin/python

import time, sys
import zmq
import urllib2

worker_addr = 'tcp://127.0.0.1:5555'
results_addr = 'tcp://127.0.0.1:5556'

print "Starting fetcher..."

ctx = zmq.Context()
worker_sock = ctx.socket(zmq.PULL)
results_sock = ctx.socket(zmq.PUSH)

worker_sock.connect(worker_addr)
results_sock.connect(results_addr)

url_opener = urllib2.build_opener()
url_opener.addheaders = [('User-agent', 'BrainSnow/0.1')]

while True:
	data = worker_sock.recv_json()
	
	try:
		f = url_opener.open(data['url'])
		print "Fetched: %s" % (data['url'])
		results_sock.send_json({'type': 'fetch', 'contents': f.read()})
	except:
		print "Could not fetch %s: %s" % (data['url'], sys.exc_info())