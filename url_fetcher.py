#! /usr/bin/python

import time
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
	data = worker_sock.recv()
	
	try:
		f = url_opener.open(data)
		print "Fetched: %s" % (data)
		results_sock.send(f.read())
	except:
		print "Could not fetch: %s" % (data)