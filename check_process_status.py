#!/usr/bin/python
#Usage etcd key/value IP:PORT
#
import urllib
import sys

def Getinfo(port):
	GetCode = urllib.urlopen("http://localhost:" + port).getcode()
	
	if GetCode == 200:
		return "1"
	else:
		return "0"

if __name__ == "__main__":
	port = sys.argv[1]
	print Getinfo(port)
