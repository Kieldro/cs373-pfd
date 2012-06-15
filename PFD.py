# HASHBANG
#?!/usr/bin/env python

import sys

# globals
DEBUG = True
dWrite = sys.stderr.write		# aliasing?
v = []

s = 0
a = 1
i = 2

class Vertex:
	"""
		class.
	"""
	def __init__ (self, v, d):
		self.value = v
		#self.k = k		# number of dependents
		self.dependents = d
		#successors = []
	 
	def __str__(self):
		# for debug
		return str(value)
		
	

def read (r):
	"""
		Read and parse input.
	"""
	
	line = r.readline()		# inputs an entire line
	tokens = line.split()		# splits string into list of string tokens
	iList = [int(x) for x in tokens]		# casts all the strings into ints
	n = iList[0]		# number of tasks
	m = iList[1]		# number of rules
	assert n <= 100, 'n too large'		# must be at least 1 task?
	assert m < n, 'm must be less than n'
	if DEBUG: dWrite('number of tasks n: {0}\n'.format(n) )		# {x} required in py 2.6
	if DEBUG: dWrite('number of rules m: {0}\n'.format(m) )
	global v		# necessary to access v in this function
	v = [Vertex(i, []) for i in xrange(n)]
	
	for i in xrange(m):
		line = r.readline()
		tokens = line.split()
		iList = [int(x) for x in tokens]
		
		target = iList[0]
		if DEBUG: dWrite('target: {0}\n'.format(target) )
		k = iList[1]		# number of dependents
		assert k > 0, 'no dependents.'		# must be at least 1 dependent?
		dependents = iList[2:]
		if DEBUG: dWrite('dependents list: {0}\n'.format(dependents) )
		v[target-1].dependents = dependents		# -1 necessary
		#if DEBUG: dWrite('v: {0}\n'.format(v) )
	return v
	
def solve ():
	"""
		solve.
	"""
	
	# find tasks with 0 dependents
	for task in v:
		if(task == []):
			if DEBUG: dWrite('len of task: {0}\n'.format(len(task) ) )
		
	

def output ():
	"""
		pydoc
	"""
	
	print 's:', s		# no str needed with ,
	print 'a:', a
	print 'i:', i
	
# ----
# main
# ----

if __name__ == "__main__":
	read(sys.stdin)
	solve()
	output()
