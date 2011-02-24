#! /usr/bin/python

import time
import zmq

fetcher_out_addr = 'tcp://127.0.0.1:5555'
fetcher_in_addr = 'tcp://127.0.0.1:5556'
parser_out_addr = 'tcp://127.0.0.1:5557'
parser_in_addr = 'tcp://127.0.0.1:5558'

first_url = "http://localhost/"

print "Starting server..."

ctx = zmq.Context()
fetcher_out_sock = ctx.socket(zmq.PUSH)
fetcher_in_sock = ctx.socket(zmq.PULL)

fetcher_out_sock.bind(fetcher_out_addr)
fetcher_in_sock.bind(fetcher_in_addr)

parser_out_sock = ctx.socket(zmq.PUSH)
parser_in_sock = ctx.socket(zmq.PULL)

parser_out_sock.bind(parser_out_addr)
parser_in_sock.bind(parser_in_addr)

while True:
	print "Pushing url: %s" % (first_url)
	fetcher_out_sock.send_json({'type': 'fetch', 'url': first_url})
	
	data = fetcher_in_sock.recv_json()
	print "Got results: %s" % (data['contents'])