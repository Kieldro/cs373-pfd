# HASHBANG
#?!/usr/bin/env python

import sys
from heapq import heappush, heappop

# globals
DEBUG = not True
dWrite = sys.stderr.write

class Vertex:
	"""
	Represents a task.
	value - task number
	dependents - list of dependent vertices as ints
	successors - list of successor vertices as ints
	usable - boolean used to mark vertex when solving
	"""
	def __init__ (self, v, d):
		self.value = v
		#self.k = k		# number of dependents
		self.dependents = d
		self.successors = []
		self.usable = True
	
	def __str__(self):
		# for debug
		return str(self.value)
		
	

def read (r):
	"""
	Reads input, parses it, and sets up all the vertices.
	r is a reader
	returns a list of vertices that represents the input file
	"""
	
	line = r.readline()		# inputs an entire line
	tokens = line.split()		# splits string into list of string tokens
	iList = [int(x) for x in tokens]		# casts all the strings into ints
	n = iList[0]		# number of tasks
	m = iList[1]		# number of rules
	assert n <= 100, 'n too large'		# must be at least 1 task?
	assert m <= 100, 'm must be less than n'
	if DEBUG: dWrite('number of tasks n: {0}\n'.format(n) )
	if DEBUG: dWrite('number of rules m: {0}\n'.format(m) )
	v = [Vertex(i+1, []) for i in xrange(n)]
	
	for i in xrange(m):
		line = r.readline()
		tokens = line.split()
		iList = [int(x) for x in tokens]
		
		target = iList[0]
		k = iList[1]		# number of dependents
		assert k >= 0, 'k must be non negative.'		# must be at least 1 dependent?
		
		dependents = iList[2:]
		v[target-1].dependents = dependents		# -1 necessary
		
		for d in dependents :
			v[d-1].successors += [target]
		
		if DEBUG: dWrite('v: {0}\n'.format([str(s) for s in v]) )

	assert len(v) == n
	return v

def solve (v) :
	"""
	Finds the proper ordering of tasks.
	v is a list of Vertex objects
	returns a list of ints as the solution
	"""
	if DEBUG: dWrite('DEBUG: solve()...\n')
	free_vertices = []
	solution = []

	# run until solution is complete
	while len(solution) != len(v):
		# add all free tasks (0 dependents) to free container
		for task in v:
			if len(task.dependents) == 0 and task.usable :
				heappush(free_vertices, (task.value, task) )
				task.usable = False

		# remove smallest vertex
		_, smallest = heappop(free_vertices)		# by virtue of heapq
		
		# apend to solution
		solution += [smallest.value]
		
		# remove smallest from successors
		for task in smallest.successors :
			assert smallest.value in v[task-1].dependents
			v[task-1].dependents.remove(smallest.value)
	
	if DEBUG: dWrite('return solution: {0}\n'.format(solution) )
	
	return solution

def output (w, solution):
	"""
	Writes the solution as a list of strings.
	w is a writer
	solution is a list of ints
	"""
	assert w is not None
	if DEBUG: dWrite('DEBUG: output()...\n')
	for s in solution :
		w.write(str(s) + ' ')
	w.write('\n')		# ok for sphere?

def run(r, w) :
	"""
	Runs the entire program.
	r is a reader
	w is a writer
	"""
	assert r is not None
	assert w is not None
	v = read(r)
	solution = solve(v)
	output(w, solution)

if __name__ == '__main__':
	run(sys.stdin, sys.stdout)
