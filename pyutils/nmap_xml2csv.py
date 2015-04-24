#! /usr/bin/python3

import sys, re
import json, getopt
import xml.etree.ElementTree as etree

def usage():
	print("\n============================================================================================")
	print("Usage:")
	print("nmap_xml2csv.py -i {input file} -o {output file}")
	print("-------------")
	print("-i | --inputfile <file>                       ### Nmap XML file")
	print("-o | --outputfile <file>                      ### file for CSV output")
	print("============================================================================================\n")

def convert(in_file, out_file):
	
	fileout=open(out_file, 'w');

	IP="N/A";
	MAC="N/A";
	Host="N/A";
	OS="N/A";
	Port="N/A";
	State="N/A";
	Banner="N/A";
	Banner2="N/A";
	CSV="";

	fileout.write("IP` MAC` Hostname` OS` Port` State` Banner` Extra Banner\n");
	tree = etree.parse(in_file);
	root = tree.getroot();
	
	for host in root.iter('host'):
		IP="N/A";
		MAC="N/A";
		Host="N/A";
		OS="N/A";
		Port="N/A";
		State="N/A";
		Banner="N/A";
		Banner2="N/A";
		# Find IP and MAC addresses
		for address in host.findall('address'):
			if address.get('addrtype') == 'mac':
				MAC=str(address.get('addr'));
			else:
				IP=str(address.get('addr'));
		# Find Hostnames
		for hostnames in host.findall('hostnames'):
			Host=hostnames.text;
		# Find OS fingerprint
		for os in host.iter('osmatch'):
			OS=str(os.attrib.get('name'));
		# Host Scripts Results, i.e: samba/nbt shares
		for hostscript in host.iter('hostscript'):
			for script in hostscript.findall('script'):
				Banner2=str(script.attrib.get('id'))+"; "+str(script.attrib.get('output'));
				for table in script.findall('table'):
					Banner2=Banner2+"; "+str(table.attrib.get('key'));
					for elem in table.findall('elem'):
						Banner2=Banner2+"; "+str(elem.attrib.get('key'))+": "+elem.text; 
				for elem in script.findall('elem'):
					Banner2=Banner2+"; "+str(elem.attrib.get('key'))+": "+elem.text;
				# CSV for hostscript results
				CSV=IP+"`"+MAC+"`"+Host+"`"+OS+"`"+""+"`"+""+"`"+""+"`"+Banner2;
				fileout.write(CSV.replace('\n', '').replace('\r', ' ')+"\n");		

		# Find Ports and Services
		for port in host.iter('port'):
			State="N/A";
			Banner="N/A";
			Port=str(port.attrib.get('protocol'))+"/"+str(port.attrib.get('portid'));
			for state in port.findall('state'):
				State=str(state.attrib.get('state'));
				#print("State: "+str(state.attrib.get('state')));
			for service in port.findall('service'):
				Banner=str(service.attrib.get('name'))+"; "+str(service.attrib.get('product'))+"; "+str(service.attrib.get('version'))+"; "+str(service.attrib.get('extrainfo'))+"; "+str(service.attrib.get('servicefp'));
				for cpe in service.findall('cpe'):
					Banner=Banner+"; "+cpe.text;
			for script in port.findall('script'):
				Banner=Banner+"; "+str(script.attrib.get('id'))+"; "+str(script.attrib.get('output'));
				for table in script.findall('table'):
					Banner=Banner+"; "+str(table.attrib.get('key'));
					for elem in table.findall('elem'):
						Banner=Banner+"; "+str(elem.attrib.get('key'))+": "+elem.text;
			# Set CSV Variable
			CSV=IP+"`"+MAC+"`"+Host+"`"+OS+"`"+Port+"`"+State+"`"+Banner;
			fileout.write(CSV.replace('\n', '').replace('\r', ' ')+"\n");
	

def main(argv):
	if len(argv)<1:
		print("Missing Arguments");
		usage();
		sys.exit(2);

	try:
		opts, args = getopt.getopt(argv, 'hi:o:', ["inputfile=", "outputfile="]);
	except getopt.GetoptError as err:
		print(err);
		usage();
		sys.exit(2);

	for opt, arg in opts:
		if opt == '-h':
			usage();
			sys.exit();
		elif opt in ('-i', "--inputfile"):
			infile = arg;
		elif opt in ('-o', "--outputfile"):
			outfile = arg;
		else:
			print("what, how did this happen?");
	convert(infile, outfile);

if __name__ == "__main__":
	main(sys.argv[1:])
