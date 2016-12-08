#! /usr/bin/python

import urllib,
import getopt, sys, re, lxml


userid
password
sessionid
#https://192.168.1.31:3780/api/1.1/xml
#header text/xml
uri="/api/1.1/xml"

def usage():
	print("\n============================================================================================")
	print("Usage:")
	print("sitelist.py -h {host} -l {login} -p {password}")
	print("-------------")
	print("-h | --host <host>			### Nexpose host")
	print("-l | --key <API KEY>		        ### Shodan API key")
	print("-p | --page <page>		        ### result page, (default)first page, or all pages") 
	print("============================================================================================\n")

def login():
#<?xml version="1.0" encoding="UTF-8"?>
#<LoginRequest user-id="nxadmin" password="nxadmin" />
	data = '<LoginRequest userid=\"'+userid+'\" password=\"'+password+'\"></LoginRequest>';
	url = host+':3780'+uri
	response = urllib.request.urlopen(url, data);

def logout():

def main(argv):
