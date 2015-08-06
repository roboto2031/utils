#! /bin/bash

#Variables
host=$1
startport=$2
stopport=$3

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
	for ((counter=$startport; counter<=$stopport; counter++))
	do
		(echo >/dev/tcp/$host/$counter) > /dev/null 2>&1 && echo "$counter open";
	done;
}

#main
pingcheck;
portcheck;
