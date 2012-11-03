# Parse an apache log file and checks for tor exit nodes.
# Takes a user specified action if one is found.
# https://trac.torproject.org/projects/tor/wiki/doc/TorDNSExitList
# http://code.google.com/p/apachelog/downloads/list

import urllib.request
import string
import re

url = "http://exitlist.torproject.org/exit-addresses"
exits = urllib.request.urlopen(url).read()
exitlist = []

for exitnode in str( exits, encoding='utf8' ).split('\n'):
    if "ExitAddress" in exitnode:
        exitlist.append(exitnode.split(' ')[1])

print(len(exitlist))


rexp = re.compile('\d+\.\d+\.\d+\.\d+')
a = rexp.match(line)
if not a is None:
a.group(1) #IP address


for line in open('/var/log/httpd/access.log','r'):
    doSomething(line

f = open('/tmp/workfile', 'w')
for line in f:

f.close()
