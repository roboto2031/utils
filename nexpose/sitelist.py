#! /usr/bin/python

import urllib.request, httplib2
import getopt, sys, re, lxml


userid=""
password=""
sessionid=""
host=""
#https://192.168.1.31:3780/api/1.1/xml
headers = {"Content-type" : "text/xml"}
uri="/api/1.1/xml"

def usage():
	print("\n============================================================================================")
	print("Usage:")
	print("sitelist.py -s {host} -l {login} -p {password}")
	print("---------------------------")
	print("-s | --server <host>			### Nexpose host")
	print("-l | --login <username>		        ### Nexpose username")
	print("-p | --password <password>		### Nexpose password") 
	print("============================================================================================\n")

def login():
#<?xml version="1.0" encoding="UTF-8"?>
#<LoginRequest user-id="nxadmin" password="nxadmin" />
	xdata = '<LoginRequest user-id=\"'+userid+'\" password=\"'+password+'\"></LoginRequest>';
	url = 'https://'+host+':3780'+uri
	req = urllib.request.Request(url, xdata, headers);
	response = urllib.request.urlopen(req);
	
	return str(response.read(), 'utf-8');

def logout():
	print ("logout");

def main(argv):
	if len(argv)<1:
		print("Missing Arguments");
		usage();
		sys.exit(2);

	try:
		opts, args = getopt.getopt(argv, 'hs:l:p:', ["server=", "login=", "password="]);
	except getopt.GetoptError as err:
		print(err);
		usage();
		sys.exit(2);

	for opt, arg in opts:
		if opt == '-h':
			usage();
			sys.exit();
		elif opt in ('-s', "--server"):
			host = arg;
		elif opt in ('-l', "--login"):
			userid = arg;
		elif opt in ('-p', "--password"):
			password = arg;
		else:
			print("what, how did this happen?");

	login();


if __name__ == "__main__":
	main(sys.argv[1:])
