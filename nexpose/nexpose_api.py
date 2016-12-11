#! /usr/bin/python

import urllib.request
import ssl, getopt, sys, re, lxml

host=""
port="3780"
userid=""
password=""
sessionid=""
headers = {"Content-type" : "text/xml"}
uri="/api/1.1/xml"

# api command
cmd=""

# set ssl/tls context --allow all certs
ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2);
ssl_context.verify_mode=ssl.CERT_NONE;

def usage():
	print("\n============================================================================================")
	print("Usage:")
	print("sitelist.py -s {host} -l {login} -p {password}")
	print("---------------------------")
	print("-s | --server <host>			### Nexpose host")
	print("-l | --login <username>		        ### Nexpose username")
	print("-p | --password <password>		### Nexpose password")
	print("-c | --command <api command>		### Nexpose api command") 
	print("============================================================================================\n")

# nexpose api url
url = 'https://'+host+':'+port+uri

def login():
	# xml POST data
	xdata = "<LoginRequest user-id=\"admin\" password=\"zero7ef\" />"
	xdata = xdata.encode('ascii');

	try:
		req = urllib.request.Request(url, xdata, headers)
		res = urllib.request.urlopen(req, context=ssl_context).read()
		print (res)
	except:
		print("error")

def logout():
	print ("logout");

def api_cmd(data):
	print ("api command");

def main(argv):
	if len(argv)<1:
		print("Missing Arguments");
		usage();
		sys.exit(2);

	try:
		opts, args = getopt.getopt(argv, 'hs:l:p:c:', ["server=", "login=", "password=", "command="]);
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
		elif opt in ('-c', "--command"):
			cmd = arg;
		else:
			print("what, how did this happen?");

	login();


if __name__ == "__main__":
	main(sys.argv[1:])
