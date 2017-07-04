#! /bin/bash


# MITM bridge

iptables -A FORWARD -m state --state RELATED,ESTABLISHED -j ACCEPT
iptables -A FORWARD -i eth0 -o eth1 -j ACCEPT
iptables -A FORWARD -i eth1 -o eth0 -j ACCEPT

# controlled 3 way tap
#iptables -A FORWARD -i eth0 -d
