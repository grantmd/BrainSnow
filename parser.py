#! /usr/bin/python

import time
import zmq
from HTMLParser import HTMLParser

worker_addr = 'tcp://127.0.0.1:5557'
results_addr = 'tcp://127.0.0.1:5558'

class FindLinks(HTMLParser):
	links = []
	
	def __init__(self):
		HTMLParser.__init__(self)
	
	def handle_starttag(self, tag, attrs):
		at = dict(attrs)
		if tag == 'a' and 'href' in at:
			self.links.push(at['href'])
	
	def parse(self, data):
		self.links = [];
		self.feed(data)
		
		return self.links
		
link_finder = FindLinks()

print "Starting parser..."

ctx = zmq.Context()
worker_sock = ctx.socket(zmq.PULL)
results_sock = ctx.socket(zmq.PUSH)

worker_sock.connect(worker_addr)
results_sock.connect(results_addr)


while True:
	print "Waiting for contents"
	data = worker_sock.recv_json()
	print "Got contents"
	
	print "Processing"
	urls = link_finder.parse(data['contents'])
	print "Processing complete"
	
	print "Sending next url(s)"
	for url in urls:
		results_sock.send_json({'type': 'fetch', 'url': url})
	print "Sent"