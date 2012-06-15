# HASHBANG
#?!/usr/bin/env python

import sys

DEBUG = True
dWrite = sys.stderr.write		# aliasing?

s = 0
a = 1
i = 2

def read (x):
	"""
		Read and parse input.
	"""
	line = raw_input()		# inputs an entire line
	tokens = line.split()		# splits string into list of string tokens
	iList = [int(x) for x in tokens]		# casts all the strings into ints
	n = iList[0]		# number of tasks
	m = iList[1]		# number of rules
	assert n <= 100, 'n too large'		# must be at least 1 task?
	assert m < n, 'm must be less than n'
	if DEBUG: dWrite('number of tasks n: {}\n'.format(n) )
	if DEBUG: dWrite('number of rules m: {}\n'.format(m) )
	tasks = [ [] ]*n		# lists of lists
	
	for i in xrange(m):
		line = raw_input()
		tokens = line.split()
		iList = [int(x) for x in tokens]
		
		target = iList[0]
		if DEBUG: dWrite('target: {}\n'.format(target) )
		k = iList[1]		# number of dependents
		assert k > 0, 'no dependents.'		# must be at least 1 dependent?
		dependents = iList[2:]
		tasks[target-1] = dependents
		if DEBUG: dWrite('tasks: {}\n'.format(tasks) )
	
def solve ():
	"""
		solve.
	"""
	
	if(True or tasks[t] == []):
		1
	

def output ():
	"""
		pydoc
	"""
	
	print 's:', s
	print 'a:', a
	print 'i:', i
	
# ----
# main
# ----

if __name__ == "__main__":
	#solve(sys.stdin, sys.stdout)
	read(0)
	output()
