#!/usr/bin/env python
import sys
import syslog
# Using the options shown in the README freeradius will export the work
# for determining good users to your script. Exit 0 is good auth, anything
# else is failed.  This means we can now do anything we want to authenticate
# a user using solely python.

#example freeradius -X output
#Exec-Program-Wait: plaintext: ['/usr/local/bin/fradiusauth.py', 'chasemp', "'1234'", '10.1.15.13'] 
#Exec-Program: returned: 0
#password will be pass

#example purposes only
#please for the love of god don't store this in plaintext
#in real life
#http://stackoverflow.com/questions/12042724/securely-storing-passwords-for-use-in-python-script
users = {'me': '1234'}

def die(msg):
    print msg + '\n'
    syslog.syslog(msg)
    sys.exit(1)

def accept(user):
    msg = 'accepting auth from: ' + user + '\n'
    print msg
    syslog.syslog(msg)
    sys.exit(0)

if len(sys.argv) < 4:
    die('not enough arguments for auth')

script, user, passwd, caller = sys.argv
#passed from radius as quoted literal
passwd = passwd.lstrip("'").rstrip("'")
if user in users:
    if users[user] == passwd:
        accept(user):

if user == 'radcheck':
    sys.exit(0)

die('implict deny no authorization')
