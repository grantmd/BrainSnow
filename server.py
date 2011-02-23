#! /usr/bin/python

import time
import zmq

worker_addr = 'tcp://127.0.0.1:5555'
results_addr = 'tcp://127.0.0.1:5556'

print "Starting server..."

ctx = zmq.Context()
worker_sock = ctx.socket(zmq.PUSH)
results_sock = ctx.socket(zmq.PULL)

worker_sock.bind(worker_addr)
results_sock.bind(results_addr)

while True:
	print "Pushing url"
	worker_sock.send("http://www.mylesgrant.com/")
	time.sleep(1)