# shodan 

import shodan
import sys

API_KEY = ""

if len(sys.argv) == 1:
	print ('Usage: %s <search query>' % sys.argv[0])
	sys.exit(0);

try:
	api = shodan.Shodan(API_KEY)
	
	query = ' '.join(sys.argv[1:])
	host = api.host(query)
	print(host)
	
	# Print general info
#	print ("""
#	IP: %s
#	Organization: %s
#	Operating System: %s
#	""" % (host['ip_str'], host.get('org', 'n/a'), host.get('os', 'n/a')))

	# Print all banners
#	for item in host['data']:
#		print ("""
#	Port: %s
#	Banner: %s
#	""" % (item['port'], item['data']))
		
except Exception as e:
	print ('Error: %s' % e)
	sys.exit(1)
