BrainSnow
================

BrainSnow is an auto-scaling web crawler and parser with a stupid name. It uses <a href="http://zeromq.org/">zeromq</a> for all message passing and automatically scales itself on your favorite cloud provider (if your favorite cloud provider is <a href="http://aws.amazon.com/ec2/">Amazon EC2</a>).

Requirements
------------

* <a href="http://python.org/">Python</a>
* <a href="http://zeromq.org/">ØMQ</a>
* <a href="https://github.com/zeromq/pyzmq/">PyZMQ</a>

Components
----------

* Server: This is the command center. It distributes messages to all the other parts, handles auto-scaling, commands nodes to update when code changes, etc. You need one of these.
* Fetcher: Takes urls from the Server, fetches them over http, and sends the results back. Not computationally intensive, but potentially bandwidth-heavy. You need *at least* one of these, probably more.
* Parser: Where the magic happens. Accepts results from the Fetchers via the Server, parses them for whatever, and sends urls back to the Server for further fetching.

TODO
----

* Parsing
* Scaling
* Better use of built-in ZMQ devices
