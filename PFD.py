# HASHBANG
#?!/usr/bin/env python

import sys

# globals
DEBUG = True
dWrite = sys.stderr.write		# aliasing?

class Vertex:
	"""
		class.
	"""
	def __init__ (self, v, d):
		self.value = v
		#self.k = k		# number of dependents
		self.dependents = d
		self.successors = []
		self.done = False
	
	def __str__(self):
		# for debug
		return str(self.value)
		
	

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
	v = [Vertex(i+1, []) for i in xrange(n)]
	
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
		
		for d in dependents :
			v[d-1].successors += [target]
		
		if DEBUG: dWrite('v: {0}\n'.format([str(s) for s in v]) )
	
	return v
	
def solve (v) :
	"""
		finds the solution
		v is a list of Vertex objects
		return a list of ints as solution
	"""
	if DEBUG: dWrite('DEBUG: solve()...\n')
	free_vertices = []
	solution = []
	
	while len(solution) != len(v):
		# find tasks with 0 dependents
		if DEBUG: dWrite('free tasks:')
		for task in v:
			if(len(task.dependents) == 0 and not task.done) :
				if DEBUG: dWrite('{0} '.format(task ))
				free_vertices += [task]

		if DEBUG: dWrite('\n\tfree_vertices: {0}'.format([str(fv) for fv in free_vertices]))

		while len(free_vertices) != 0:
			# find smallest vertex		
			smallest = free_vertices[0]
			for task in free_vertices :
				if (task.value < smallest.value) :
					smallest = task
			if DEBUG: dWrite('\n\tSmallest: {0}\n'.format(smallest))

			solution += [smallest.value]
			free_vertices.remove(smallest)
			if DEBUG: dWrite('\tremoved from free: {0}\n'.format(smallest.value) )
			smallest.done = True
			
			# remove smallest from successors
			print smallest.value
			if DEBUG: dWrite('\tsmallest.successors: {0}\n'.format(smallest.successors) )
			for task in smallest.successors :
				if DEBUG: dWrite('\ttask: {0}\n'.format(task ) )
				if DEBUG: dWrite('\tv[task-1].dependents: {0}\n'.format(v[task-1].dependents) )
				if smallest.value in v[task-1].dependents:
					v[task-1].dependents.remove(smallest.value)
	
	
	if DEBUG: dWrite('return solution: {0}\n'.format(solution) )

	return solution

def output (w, solution):
	"""
		output() function writes the solutions list as a string.
	"""
	if DEBUG: dWrite('DEBUG: output()...\n')
	for s in solution :
		w.write('{0} '.format(s) )
	w.write('\n')		# ok for sphere?

# ----
# main
# ----

if __name__ == "__main__":
	w = sys.stdout
	r = sys.stdin
	
	v = read(r)
	solution = solve(v)
	output(w, solution)
