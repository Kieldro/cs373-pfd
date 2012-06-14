# HASHBANG
#?!/usr/bin/env python

def read ():
	"""
	No parameters
	"""
	s = raw_input()		# inputs an entire line
	print 's: ' + s
	
	a = s.split()		# splits string into list of string tokens
	print 'a: ' + str(a)
	
	i = [int(x) for x in a]		# casts all the strings into ints
	print "i: " str(i)


# ----
# main
# ----

if __name__ == "__main__":
	#import sys
	#solve(sys.stdin, sys.stdout)
	read()
