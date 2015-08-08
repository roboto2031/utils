#! /bin/bash

#usage message
function usage
{
	echo "usage message";
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
