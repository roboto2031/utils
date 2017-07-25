#! /usr/bin/python

import sys, getopt
import hashlib

def usage():
	print("\n=======================================================================================")
	print("Usage:")
	print("hash_search.py -c hash -f hashfile")
	print("-------------")
	print("-c | --code <hash>                    ### Hash to compare with")
	print("-f | --file <hash file>               ### File of hashes")
	print("=======================================================================================\n")

def main(argv):
	hash_code="";
	hfile="";

	if len(argv)<1:
		print("Missing Arguments")
		usage()
		sys.exit(2)
	
	# arg parse block, try to get cli arguments
	try:
		opts, args = getopt.getopt(argv, 'hc:f:', ["code=", "file="])
	except getopt.GetoptError as err:
		print(err)
		usage()
		sys.exit(2)
	
	for opt, arg in opts:
		if opt == '-h':
			usage()
			sys.exit()
		elif opt in ('-c', "--code"):
			hash_code = arg;
		elif opt in ('-f', "--file"):
			hfile = arg;
		else:
			print("what, how did this happen")
	
	# base encode/decode functions
	try:
                hashes = open(hfile, 'r');
                print("===|Searching|===");
                for line in hashes.readlines():
                    hashline=line.strip('\r').strip('\n');
                    if hash_code in hashline:
                        print("+++Found hash match: " + hashline);

	except Exception:
		print(hash_code)
		print("Hmm, hashing is difficult.")
		sys.exit(2)
	
	# output encode/decode results


if __name__ == "__main__":
	main(sys.argv[1:])
