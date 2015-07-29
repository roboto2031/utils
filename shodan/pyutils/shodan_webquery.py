#! /usr/bin/python3

import sys, re, socket
import urllib.request
import json, getopt

#https://api.shodan.io/shodan/host/search?key={YOUR_API_KEY}&query={query}&facets={facets}&page={page}

API_KEY="";

def usage():
	print("\n============================================================================================")
	print("Usage:")
	print("shodan_webquery.py -k {API key} -q {search query} -f {output file} -p {page #|all} ")
	print("-------------")
	print("-k | --key <API KEY>		        ### Shodan API key")
	print("-q | --query <query>                    ### Shodan Search query")
	print("-f | --file <file>                      ### file for CSV output")
	print("-p | --page <page>		        ### result page, (default)first page, or all pages") 
	print("---  Multiple files are generated for mulit-page results. { filename.1 }")
	print("============================================================================================\n")

def shodan_query(query, key, page):
	url='https://api.shodan.io/shodan/host/search?key='+key+'&query='+query+'&page='+str(page);\
	print(url)
	response = urllib.request.urlopen(url);
	html = str(response.read(), 'utf-8');
	results=json.loads(html);

	return results;

def toFile(data, out):
	fileout=open(out, 'w');
	fileout.write("IP` Hostnames` Organization` ASN` OS` Port` Banner\n");
	
	for host in data['matches']:
		fileout.write(str(host.get('ip_str', "n/a"))+"` "+str(host.get('hostnames', "n/a"))+"` "+str(host.get('org', "n/a"))+"` "+str(host.get('asn', "n/a"))+"` "+str(host.get('os', "n/a"))+"` "+str(host.get('port', "n/"))+"` ["+str(host.get('data', "n/a")).replace('\n', '').replace('\r', ' ')+"]\n");

def toScreen(data):
	for host in data['matches']:
		print("IP: %s" %(str(host.get('ip_str', "n/a"))));
		print("Hostnames: %s" %(str(host.get('hostnames', "n/a"))));
		print("Organiztion: %s" %(str(host.get('org', "n/a"))));
		print("AS: %s" %(str(host.get('asn', "n/a"))));
		print("OS: %s" %(str(host.get('os', "n/a"))));
		print("Port: %s" %(str(host.get('port', "n/a"))));
		print("Banner: %s" %(str(host.get('data', "n/a")+"\n")));

def main(argv):
	isCSV=0;
	page='1';

	if len(argv)<1:
		print("Missing Arguments");
		usage();
		sys.exit(2);

	try:
		opts, args = getopt.getopt(argv, 'hk:q:f:p:', ["key=", "query=", "file=", "page="]);
	except getopt.GetoptError as err:
		print(err);
		usage();
		sys.exit(2);

	for opt, arg in opts:
		if opt == '-h':
			usage();
			sys.exit();
		elif opt in ('-k', "--key"):
			API_KEY = arg;
		elif opt in ('-q', "--query"):
			query = arg;
		elif opt in ('-f', "--file"):
			outfile = arg;
			isCSV=1;
		elif opt in ('-p', "--page"):
			if arg=="":
				page='1'
			else:
				page=str(arg);
		else:
			print("what, how did this happen?");

	# get page 1 of results
	if page=="all":
		results=shodan_query(query, API_KEY, '1');
	else:
		results=shodan_query(query, API_KEY, page);

	if isCSV == 1:
		toFile(results, outfile+'.1');
	else:
		toScreen(results);

	# find max pages
	max_page=int((results['total']/100));
	if (results['total']%100) > 0:
		max_page=max_page + 1;
	print ("Total Results: "+str(results['total']));
	print ("Pages: "+str(max_page));
	
	if page=="all":
		# for loop through additional result pages
		for page in range(2, max_page+1):
			results=shodan_query(query, API_KEY, page);
			if isCSV == 1:
				print("Page: "+str(page));
				toFile(results, outfile+'.'+str(page));
			else:
				toScreen(results);


if __name__ == "__main__":
	main(sys.argv[1:])


