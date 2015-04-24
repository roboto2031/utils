#! /usr/bin/python

#https://google.com/safebrowsing/diagnostic?site=123news.pw

import sys
import urllib
import urllib2
import json


domain= sys.argv[1]

url= 'https://google.com/safebrowsing/diagnostic?site='+domain
print "domain is",domain
print url

request=urllib2.Request(url)
request_opener = urllib2.build_opener()
response = request_opener.open(request)
response_data = response.read()
print response_data
#json_result = json.loads(response_data)
#result_list = json_result['d']['results']
#print results_list


