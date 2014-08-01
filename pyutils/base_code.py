#! /usr/bin/python

import sys, getopt
import base64

def usage():
	print("\n=======================================================================================")
	print("Usage:")
	print("base_code.py -b 64|32|16 -e string -d code")
	print("-------------")
	print("-b | --base <format>                    ### encoding format [16,32,64]")
	print("-e | --encode <binary string>           ### encodes a binary string with defined format")
	print("-d | --decode <base encoded string>     ### decodes encoded string using defined format")
	print("=======================================================================================\n")

def main(argv):
	encode=0
	decode=0
	data=0
	encoding='0'

	if len(argv)<1:
		print("Missing Arguments")
		usage()
		sys.exit(2)
	
	# arg parse block, try to get cli arguments
	try:
		opts, args = getopt.getopt(argv, 'hb:e:d:', ["base=", "encode=", "decode="])
	except getopt.GetoptError as err:
		print(err)
		usage()
		sys.exit(2)
	
	for opt, arg in opts:
		if opt == '-h':
			usage()
			sys.exit()
		elif opt in ('-b', "--base"):
			encoding = arg
		elif opt in ('-e', "--encode"):
			str = arg
			encode=1
		elif opt in ('-d', "--decode"):
			code = arg
			decode=1
		else:
			print("what, how did this happen")
	
	# base encode/decode functions
	try:
		if (encode == decode):
			print("must use only one function, encode or decode")
			usage()
			sys.exit(2)
		if (encoding == '16' and decode == 1):
			data=base64.b16decode(code)
		elif (encoding == '16' and encode == 1):
			data=base64.b16encode(str.encode())
		elif (encoding == '32' and decode == 1):
			data=base64.b32decode(code)
		elif (encoding == '32' and encode == 1):
			data=base64.b32encode(str.encode())
		elif (encoding == '64' and decode == 1):
			data=base64.b64decode(code)
		elif (encoding == '64' and encode == 1):
			data=base64.b64encode(str.encode())
		else:
			print("How did you get here, GTFO")
			usage()
			sys.exit(2)
	except Exception:
		print(code)
		print("Is this actually encoded? Check padding")
		sys.exit(2)
	
	# output encode/decode results
	print(data)


if __name__ == "__main__":
	main(sys.argv[1:])
