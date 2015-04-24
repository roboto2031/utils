#! /usr/bin/python3

import sys, re, socket
import urllib.request
import json, getopt

#https://api.shodan.io/shodan/host/{ip}?key={YOUR_API_KEY}

API_KEY="";

def usage():
	print("\n============================================================================================")
	print("Usage:")
	print("shodan_web.py -t {IP} ")
	print("-------------")
	print("-t | --target <IP>                    ### Shodan Host Lookup")
	print("============================================================================================\n")

def shodan_host(query, key):
	url='https://api.shodan.io/shodan/host/'+query+'?key='+key;

	response = urllib.request.urlopen(url);
	html = str(response.read(), 'utf-8');
	host=json.loads(html);
	print("IP: %s" %(str(host.get('ip_str', "n/a"))));
	print("Hostnames: %s" %(str(host.get('hostnames', "n/a"))));
	print("Organization: %s" %(str(host.get('org', "n/a"))));
	print("AS: %s" %(str(host.get('asn', "n/a"))));
	print("OS: %s" %(str(host.get('os', "n/a"))));
	print("Ports: %s" %(str(host.get('ports', "n/a"))+"\n"));
	for item in host['data']:
		print("Product: %s" %(str(item.get('product', "n/a"))));
		print("Title: %s" %(str(item.get('title' ,"n/a"))));
		print("Timestamp: %s" %(str(item.get('timestamp', "n/a"))));
		print("cpe: %s" %(str(item.get('cpe', "n/a"))));
		print("Version: %s" %(str(item.get('version', "n/a"))));
		print("Port: %s" %(str(item.get('port', "n/a"))));
		print("DATA: %s" %(str(item.get('data', "n/a"))));

def main(argv):

	if len(argv)<1:
		print("Missing Arguments");
		usage();
		sys.exit(2);

	try:
		opts, args = getopt.getopt(argv, 'ht:', ["target="]);
	except getopt.GetoptError as err:
		print(err);
		usage();
		sys.exit(2);

	for opt, arg in opts:
		if opt == '-h':
			usage();
			sys.exit();
		elif opt in ('-t', "--target"):
			query = arg;
		else:
			print("what, how did this happen?");

	shodan_host(query, API_KEY);

if __name__ == "__main__":
	main(sys.argv[1:])
