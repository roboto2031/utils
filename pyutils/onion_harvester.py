#! /usr/bin/python

import itertools
import sys, io, getopt
import socket
import urllib.request
from threading import Thread

# character space [a-z,2-7]
# string length 16

#### TO DO ####
# Threading   #
# Socks Proxy #
# File Output #
###############

def header():
	print("=========[ Onion Harvester ]==========")
	print("=      Brute Forces Onion Names      =")
	print("=      Outputs to a CSV file         =")
	print("=------------------------------------=")
	print("=      Let's dig up some Onions      =")
	print("=                                    =")
	print("======================================")


def ver_chk():
	if sys.version_info < (3, 0):
		print("Not Python 3. This script may FAIL")

def conn_scan(host, port):
	try:
		sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.connect((host,port))
		sock.send(b'knock knock\r\n')
		result=sock.recv(100)
		print("port %d open"% port)
		print(str(result))
		sock.close()
	except:
		print("no connection")

def onion_scan(onion, ports):
	onion=onion+".onion"
	print(onion)
	ip=socket.gethostbyname(onion)
	
	try:
		ip=socket.gethostbyname(onion)
	except:
		print("no IP")
	
	for port in ports:
		print("scanning port " + str(port))
		conn_scan(ip, port)

def brute_onion(ports):
	str=itertools.permutations('abcdefghijklmnopqrstuvwxyz234567', 16)
	for i in str:
		onion_scan(''.join(i), ports)

def main():
	default_ports=[21, 22, 23, 25, 80, 443]
	ports=default_ports;

	if len(argv)<1:
		print("Missing Arguments")
		usage()
		sys.exit(2)
	
	# arg parse block, try to get cli arguments
	try:
		opts, args = getopt.getopt(argv, 'h:b:p:f:', ["host=", "bruteforce=", "ports=", "file="])
	except getopt.GetoptError as err:
		print(err)
		usage()
		sys.exit(2)
	
	for opt, arg in opts:
		if opt == ('-h' "--host"):
			brute = 0
			host = arg
		elif opt in ('-b', "--bruteforce"):
			brute = 1
		elif opt in ('-p', "--ports"):
			ports = arg
		elif opt in ('-f', "--file"):
			file = arg
		else:
			print("what, how did this happen")
	if brute == 0:
		hostIP = socket.gethostbyname(host)
		for port in ports:
			print("scanning port " + str(port))
			conn_scan(hostIP, port);
	else:
	 	brute_onion(ports);


#ver_chk();
header();
main();