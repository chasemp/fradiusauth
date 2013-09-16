#!/usr/bin/env python
import sys
from radius import RADIUS

if len(sys.argv) < 5:
    print 'pass in args: <radius_host> <radius_secret> <username> <userpass>

script, host, secret, name, passwd = sys.argv

r = RADIUS(secret, host, 1812)

if r.authenticate(name, passwd):
    print "%s authenticated" %s (name,)

print "Authentication Failed"
