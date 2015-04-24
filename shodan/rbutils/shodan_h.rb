#! /usr/bin/ruby

require 'shodan'

# API KEY
api=Shodan::Shodan.new("");

ip=ARGV[0]

host=api.host(ip);

puts ("IP: "+host['ip_str'].to_s)
puts ("Hostnames: "+host['hostnames'].to_s)
puts ("Organization: "+host['org'].to_s)
puts ("AS: "+host['asn'].to_s)
puts ("OS: "+host['os'].to_s)
puts ("Ports: "+host['ports'].to_s+"\n\n")
host['data'].each{ |data|
	puts ("Product: "+data['product'].to_s)
	puts ("Title: "+data['title'].to_s)
	puts ("TimeStamp: "+data['timestamp'].to_s)
	puts ("cpe: "+data['cpe'].to_s)
	puts ("Version: "+data['version'].to_s)
	puts ("Port: "+data['port'].to_s)
	puts "DATA:",data['data'],"\n"
}

