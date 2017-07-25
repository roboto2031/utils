#! /usr/bin/python

import sys, getopt
import hashlib

def usage():
	print("\n=======================================================================================")
	print("Usage:")
	print("fizzy_hash.py -c hash -a algorithim -w wordlist")
	print("-------------")
	print("-c | --code <hash>                    ### Hash to compare with")
	print("-a | --algo <hash algorithim>         ### Hashing algorithim [md5|sha1]")
	print("-w | --wordlist <wordlist>            ### words for hash comparison")
	print("=======================================================================================\n")

def main(argv):
	hash_code="";
	wordlist="";
	algo="";

	if len(argv)<1:
		print("Missing Arguments")
		usage()
		sys.exit(2)
	
	# arg parse block, try to get cli arguments
	try:
		opts, args = getopt.getopt(argv, 'hc:a:w:', ["code=", "algo=", "wordlist="])
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
		elif opt in ('-a', "--algo"):
			algo = arg;
		elif opt in ('-w', "--wordlist"):
			wordlist = arg;
		else:
			print("what, how did this happen")
	
	# base encode/decode functions
	try:
                if (algo == 'md5'):
                    hash_type = hashlib.md5();
                elif (algo == 'sha1'):
                    hash_type = hashlib.sha1();
                else:
                    print("Need a hashing algorthim");
                    usage();
                    sys.exit(2);

                word_file = open(wordlist, 'r');
                print("===|Searching|===");
                for line in word_file.readlines():
                    word=line.strip('\r').strip('\n');
                    hash_type.update(word.encode());
                    if hash_code in hash_type.hexdigest():
                        print("+++Found hash match: " + word + ":" + hash_type.hexdigest());

	except Exception:
		print(hash_code)
		print("Hmm, hashing is difficult.")
		sys.exit(2)
	
	# output encode/decode results


if __name__ == "__main__":
	main(sys.argv[1:])
