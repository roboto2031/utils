#! /usr/bin/python

# listen for dns requests for various subdomains
# take subdomain and piece together the file.

import socket
import sys

domain="iamev.il";
request="";
subdomain="";
response="127.0.0.1"

if domain in request:
	subdomain=request.split('.');
else:
	response=gethostbyname(request);
