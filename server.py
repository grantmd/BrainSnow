#! /usr/bin/python

import time
import zmq

worker_addr = 'tcp://127.0.0.1:5555'
results_addr = 'tcp://127.0.0.1:5556'
first_url = "http://localhost/"

print "Starting server..."

ctx = zmq.Context()
worker_sock = ctx.socket(zmq.PUSH)
results_sock = ctx.socket(zmq.PULL)

worker_sock.bind(worker_addr)
results_sock.bind(results_addr)

while True:
	print "Pushing url: %s" % (first_url)
	worker_sock.send(first_url)
	
	data = results_sock.recv()
	print "Got results: %s" % (data)