# shodan

import shodan
import sys

API_KEY = ""

if len(sys.argv) == 1:
	print('Usage: %s <search query>' % sys.argv[0])
	sys.exit(0);

try:
	api = shodan.Shodan(API_KEY)
	page_num=1
	query = ' '.join(sys.argv[1:])
	result = api.search(query,limit=100,page=page_num)
	page_max=((result['total'])/100)

	print('Result found: %s' % result['total'])
	for service in result['matches']:
		
		print("""
		IP: %s
		OS: %s
		Hostnames: %s
		""" % (service['ip_str'], service['os'], service['hostnames']))

except Exception as e:
	print('Error: %s' % e)
	sys.exit(1)
