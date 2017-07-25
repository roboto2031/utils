#!/usr/bin/python

from passlib.hash import sha512_crypt

rounds=50000;
clear_pass
hash = sha512_crypt.encrypt(clear_pass, rounds=rounds);
print(hash);
