#! /bin/bash

FILE=$1
LOC=$2

for ip in $(cat $FILE); do
	wget -w 5 --passive-ftp --random-wait --limit-rate=5k -t 5 -r -P $LOC -A jpg,jpeg,gif,png ftp://$ip
	echo $ip >> $LOC/downloaded.lst;
	sed -i -e "/$ip/d" $FILE;
done;
