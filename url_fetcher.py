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
	print "Waiting for url"
	data = worker_sock.recv_json()
	print "Got: %s" % (data['url'])
	
	try:
		print "Fetching"
		f = url_opener.open(data['url'])
		print "Fetched"
		
		print "Sending contents"
		results_sock.send_json({'type': 'fetch', 'contents': f.read()})
		print "Sent"
	except:
		print "Could not fetch %s: %s" % (data['url'], sys.exc_info())