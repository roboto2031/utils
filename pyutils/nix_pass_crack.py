# passwd crack

import crypt


def testPass(cryptPass):
	salt = cryptPass[0:2]
	dictfile = open('dictionary.txt','r')
	for word in dictfile.readlines():
		word = word.strip('\n')
		cryptword = crypt.crypt(word,salt)
		if (cryptword == cryptPass):
			print ("[+] Found Password: "+word+"\n")
			return
	print ("[-] Password Not Found.\n")
	return


def main():
	passfile = open('passwords.txt')
	for line in passfile.readlines:
		if ":" in line:
			user = line.split(':')[0]
			cryptPass = line.split(':')[1].strip(' ')
			print ("[*] Cracking Password for: "+user)
			testPass(cryptPass)

if __name__ == "__main__":
	main()