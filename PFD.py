# HASHBANG
#?!/usr/bin/env python

s = 0
a = 1
i = 2

def read (x):
	"""
		No parameters
	"""
	s = raw_input()		# inputs an entire line
	
	a = s.split()		# splits string into list of string tokens
	
	i = [int(x) for x in a]		# casts all the strings into ints


def pfdPrint ():
	"""
		pydoc
	"""
	
	print 's: ' + str(s)
	print 'a: ' + str(a)
	print "i: " + str(i)
	
# ----
# main
# ----

if __name__ == "__main__":
	#import sys
	#solve(sys.stdin, sys.stdout)
	read(0)
	pfdPrint()
