#! /usr/bin/python

import getopt, time, sys
import ftplib

def anonlogin(hostname):
	try:
		ftp= ftplib.FTP(hostname);
		ftp.login('anonymous', 'anon@place.net');
		print("Success: Anonymous Login");
		ftp.quit();
		return True;
	except ftplib.
