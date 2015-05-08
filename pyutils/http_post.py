#! /usr/bin/python

import getopt, sys
from urllib.parse import urlencode
import httplib2

def usage():
	print("\n=======================================================================================");
	print("Usage:");
	print("http_post.py -t URL -m message");
	print("-------------");
	print("-t | --target <URL>                    ### Target URL");
	print("-m | --message <message>               ### Message to use in POST requet");
	print("=======================================================================================\n");
        
def main(argv):
        target="";
        message={};
        headers={'Content-Type': 'application/x-www-form-urlencoded'};
        
        if len(argv)<1:
            print("Missing Arguments");
            usage();
            sys.exit(2);
	
        # arg parse block, try to get cli arguments
        try:
            opts, args = getopt.getopt(argv, 'ht:m:', ["target=", "message="]);

        except getopt.GetoptError as err:
            print(err);
            usage();
            sys.exit(2);

        for opt, arg in opts:
            if opt == '-h':
                usage();
                sys.exit();
            elif opt in ('-t', "--target"):
                target = arg;
            elif opt in ('-m', "--message"):
                str = arg.replace("'", "");
                for i in str.split(','):
                    param, value=i.split(':');
                    message[param.strip()]=value.strip();
            else:
                print("what, how did this happen");
	
	# Send POST request
        hconn = httplib2.Http('.cache');
        response, content = hconn.request(target, 'POST', urlencode(message), headers=headers);
        print(content.decode('utf-8'));

if __name__ == "__main__":
    main(sys.argv[1:]);
