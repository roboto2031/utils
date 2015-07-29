#! /usr/bin/python

import itertools
import sys
import socket
import urllib.request

# character space [a-z,2-7]
# string length 16

#### TO DO ####
# Threading   #
# Socks Proxy #
# Port list   #
# File Output #
###############


def ver_chk():
	if sys.version_info < (3, 0):
		print("Not Python 3. This script may FAIL")

def test_onion(onion):
	sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	onion=onion+".onion"
	print(onion)
	ip=socket.gethostbyname(onion)
	
	try:
		result=sock.connect_ex((ip,80))
		if result == 'None':
			print("port 80 open")
		else:
			print("closed")
	except:
		print("no connection")
	
	

def main():
	str=itertools.permutations('abcdefghijklmnopqrstuvwxyz234567', 16)
	for i in str:
		test_onion(''.join(i))


#ver_chk();
main();