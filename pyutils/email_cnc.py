### script -> base64 -> pgp -> email <- pgp <- base64 <- execute
### create script/code, encode to base64, encrypt with pgp and sign, send email to bot account
### bot recieves email, decrpyt pgp and verify sig, decode base 64, execute script/code

import sys
import imaplib
import getpass
import email
import datetime

E_address="<insert email address>"
M = imaplib.IMAP4_SSL('imap.gmail.com')

try:
	M.login(E_address, getpass.getpass())
except imaplib.IMAP4.error:
	print (" Login Failed");
	exit(0);

rv, mailboxes = M.list()
if rv == 'OK':
	print("Mailboxes:")
	print(mailboxes)

# Note: This function definition needs to be placed
#       before the previous block of code that calls it.
def process_mailbox(M):
	rv, data = M.search(None, "ALL")
	if rv != 'OK':
		print ("No messages found!")
		return

	for num in data[0].split():
		rv, data = M.fetch(num, '(RFC822)')
		if rv != 'OK':
			print ("ERROR getting message", num)
			return

		print(data[0][1])
		msg = email.message_from_string(data[0][1])
		print(msg)
		print ('Message %s: %s' % (num, msg['Subject']))
		print ('Raw Date:', msg['Date'])
		date_tuple = email.utils.parsedate_tz(msg['Date'])
		if date_tuple:
			local_date = datetime.datetime.fromtimestamp(
			email.utils.mktime_tz(date_tuple))
			print ("Local Date:", \
			local_date.strftime("%a, %d %b %Y %H:%M:%S"))


rv, data = M.select("command")
if rv == 'OK':
	print("Processing Mailbox...\n")
	process_mailbox(M)
	M.close()
M.logout()


