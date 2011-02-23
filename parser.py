#! /usr/bin/python

import time
import zmq

worker_addr = 'tcp://127.0.0.1:5557'
results_addr = 'tcp://127.0.0.1:5558'

print "Starting parser..."

ctx = zmq.Context()
worker_sock = ctx.socket(zmq.PULL)
results_sock = ctx.socket(zmq.PUSH)

worker_sock.connect(worker_addr)
results_sock.connect(results_addr)


while True:
	data = worker_sock.recv()
	print "Got: %s" % (data)