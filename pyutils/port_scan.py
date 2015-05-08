#! /usr/bin/python

# port scan

import io, getopt
import sys, socket
from threading import Thread

def connScan(tgtHost, tgtPort):
	try:
		connsock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		connsock.connect((tgtHost, tgtPort))
		connsock.send(b'knockknock\r\n')
		results=connsock.recv(100)
		print("port %d open"% tgtPort)
		print("banner \n" + str(results))
		connsock.close()
	except:
		print("port %d close"% tgtPort)

def portScan(tgtHost, tgtPorts):
	try:
		tgtIP=socket.gethostbyname(tgtHost)
	except:
		print("unable to resolve host")
		return
	
	try:
		tgtName=socket.gethostbyaddr(tgtIP)
	except:
		print("unable to resolve IP")
	
	socket.setdefaulttimeout(1)
	
	#connScan(tgtHost, tgtPorts)
	for tgtPort in tgtPorts:
		print("scanning port " + str(tgtPort))
		connScan(tgtHost, tgtPort)

ports=[80, 443, 21]
portScan("google.com", ports)