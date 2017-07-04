# crack and unzip file

import zipfile
import sys
from threading import Thread

# extract file with password
def extractFile(zfile, password):

	try:
		zFile.extractall(pwd=password)
		return password
	except Exception as e:
		return


def main():
	file=sys.argv[1]
	passfile=open(sys.argv[2], 'r')
	zFile = zipfile.ZipFile(file)

	for line in passfile.readlines():
		password = line.strip('\n').encode()
		guess = extractFile(zFile, password)
		if guess:
			print ('[+] Password = ' + password + '\n')
			exit(0)

if __name__ == '__main__':
	main()
