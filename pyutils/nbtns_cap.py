#!/usr/bin/python

import socket

def decode(nbname):
    if len(nbname) != 32:
        return nbname
    l = []
    for i in range(0, 32, 2):
        l.append(chr(((ord(nbname[i]) - 0x41) << 4) |
                     ((ord(nbname[i + 1]) - 0x41) & 0xf)))
    return ''.join(l).split('\x00', 1)[0]

port=137

sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM);
sock.bind(("0.0.0.0", port));

while(True):
        data, addr=sock.recvfrom(1024);
        #print("recevied: ", data);
        nbname=str(data).split(' ')[1].strip('\\x00');
        print("Who is:", decode(nbname))
        print("Request from:", addr[0]);

