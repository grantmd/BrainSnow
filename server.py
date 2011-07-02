#! /usr/bin/python

import time
import zmq

fetcher_out_addr = 'tcp://127.0.0.1:5555'
fetcher_in_addr = 'tcp://127.0.0.1:5556'
parser_out_addr = 'tcp://127.0.0.1:5557'
parser_in_addr = 'tcp://127.0.0.1:5558'

next_url = "http://localhost/"

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
	print "Pushing url: %s" % (next_url)
	fetcher_out_sock.send_json({'type': 'fetch', 'url': next_url})
	print "Pushed"
	
	print "Waiting for results"
	data = fetcher_in_sock.recv_json()
	print "Got results"
	
	print "Sending results to parser"
	parser_out_sock.send_json({'type': 'parse', 'contents': data['contents']})
	print "Sent"
	
	print "Waiting for next url from parser"
	data = parser_in_sock.recv_json()
	next_url = data['url']
	print "Got next url"
	