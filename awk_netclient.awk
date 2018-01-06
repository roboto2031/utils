#! /bin/awk -f
{ service = "/inet/tcp/0/172.30.128.61/4321"
print $0 |& service 
close(service) }
