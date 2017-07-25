#!/bin/bash

USER=$1
HOST=$2
shift
shift
#ssh $USER@$HOST;
for ARG in "$@"
do
	sleep 5;
	echo "knock knock";
        nmap -Pn --host_timeout 100 --max-retries 0 -p $ARG $HOST > /dev/null;
done
#sleep 2;
#ssh $USER@$HOST;
exit 0;
