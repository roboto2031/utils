#! /bin/bash

HOST=$1
EXT=$2
LOC=$3

torify wget -w 5 --limit-rate=5k -r -A jpg,jpeg,gif,png ftp://$HOST -e use_proxy=yes -e ftp_proxy=127.0.0.1:8118
