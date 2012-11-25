# Parse an apache acess log and checks for tor exit nodes.
# TODO: add hidemyass.com check

import fileinput
import re
import string
import sys
import urllib.request

def getTorExits():
	# https://trac.torproject.org/projects/tor/wiki/doc/TorDNSExitList
	# http://code.google.com/p/apachelog/downloads/list
	url = "http://exitlist.torproject.org/exit-addresses"
	exits = urllib.request.urlopen(url).read()
	exitlist = []

	for exitnode in str( exits, encoding='utf8' ).split('\n'):
		if "ExitAddress" in exitnode:
			exitlist.append(["Tor Exit", exitnode.split(' ')[1]])

	return exitlist
	
def getHMAProxies():
	return []
	
def printProxies(prox): 
	for node in proxies:
		print(node)
	print(len(proxies))

def getAddressFromLog(line):
	ip = re.match("^\d+\.\d+\.\d+\.\d+", line)
	return ip.group(0).strip()

if len(sys.argv) != 2 :
	print("Usage: python torhound.py ACCESS_LOG")
	sys.exit()

proxies = []
proxies += getTorExits()
proxies += getHMAProxies()

#printProxies()

for line in fileinput.input(sys.argv[1]):
	ip = getAddressFromLog(line)
	for prox in proxies:
		if ip == prox[1]:
			print(prox[0] + " found: " + prox[1])
