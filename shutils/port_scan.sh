#!/bin/bash

#usage message
function usage
{
	echo "|==============================================================================|";
	echo "| [port_scan.sh -t <target IP> -f <start port> -l <stop port> -p <tcp|udp> -h] |";
	echo "|------------------------------------------------------------------------------|";
	echo "| -h                          #### help/usage message, this thing.         ####|";
	echo "| -t <target IP>	      #### The IP of the target to be scanned.     ####|";
	echo "| -f <start port>             #### The first port in the port range.       ####|";
	echo "| -l <stop port>              #### The last port in the port range.        ####|";
	echo "| -p <tcp|udp>                #### The protocol to be used, TCP or UDP.    ####|";
	echo "|==============================================================================|";
}

#ping
function pingcheck
{

	ping=`ping -c 1 $host | grep bytes | wc -l`
	if [ "$ping" -gt 1 ]; then
		echo "$host is up";
	else
		echo "$host is down quitting";
		exit;
	fi
}

#port check
function portcheck
{
	if [ $proto == "tcp" ]; then
		for ((counter=$startport; counter<=$stopport; counter++))
		do
			(echo >/dev/tcp/$host/$counter) > /dev/null 2>&1 && echo "$counter open";
		done;
	elif [ $proto == "udp" ]; then
		for ((counter=$startport; counter<=$stopport; counter++))
		do
			(echo >/dev/udp/$host/$counter) > /dev/null 2>&1 && echo "$counter open";
		done;
	else
		echo "please specify a protocol";
		usage;
		exit;
	fi	
}	

#main
if [ $# -eq 0 ]; then
	echo "Missing Option";
	usage;
	exit;
fi
while getopts  "ht:f:l:p:" opt; do
	case $opt in
		h)	# usage message
			usage;
			exit;
			;;
		t)	# target
			host=$OPTARG;
			;;
		f)	# first port
			startport=$OPTARG;
			;;
		l)	# last port
			stopport=$OPTARG;
			;;
		p)	# protocol
			proto=$OPTARG;
			;;
		\?)	# unknown option
			echo "Invalid option -$OPTARG" >&2;
			usage;
			exit 1;
			;;
	esac
done;
pingcheck;
portcheck;
