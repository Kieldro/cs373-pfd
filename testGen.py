import random
import collections

w = sys.stdout

def generate_output (n, m) :
	"""
	Generates an output file. 
	NOTE: RunPDF.out is incorrect. 
	Feed that file into PDF to output the correct output file.
	n is the number of tasks
	m is the number of rules
	returns answer in form of int list.
	"""
	answer = range(1, n+1)
	random.shuffle(answer)
	out = open('RunPFD.out', 'w')
	for a in answer :
		out.write("{0} ".format(a))
	out.close()
	return answer

def generate_input (n, m, output) :
	"""
	Generates the input file.
	n is the number of tasks
	m is the number of rules
	output is the output file to match
	"""
	inpt = open('RunPFD.in', 'w')
	inpt.write("{0} {1}\n".format(n, m))
	
	# decide which vertices will get rules
	random_indices = random.sample(xrange(1, len(output)), m)
	random_indices.sort()
	random_elems = []
	for i in random_indices :
		random_elems += [output[i]]
	rule_vertices = collections.deque(random_elems)
	
	dq = collections.deque(output)
	previous = collections.deque()
	
	w.write("\n\nDeque: " + str(dq))
	while len(rule_vertices) > 0 :
		# Pop from dq and insert to previous until
		# we get a vertex with a rule.
		current_rule = rule_vertices.popleft()
		current_num = dq.popleft()
		while current_rule != current_num :
			previous.append(current_num)
			current_num = dq.popleft()
			
			
		# Produce the dependencies (from the deque 'previous').
		assert current_rule == current_num
		num_dependencies = random.randrange(0, len(previous))
		dependencies = random.sample(previous, num_dependencies)
		assert dependencies.count(previous[-1]) <= 1
		# 	Add previous task in ouput, if not already there.
		if dependencies.count(previous[-1]) == 0 :	
			dependencies += [previous[-1]]
		
		previous.append(current_num) # We're done with this number
		
		# Ouput a rule line.
		inpt.write("{0} {1} ".format(current_rule, len(dependencies)))
		for d in dependencies :
			inpt.write("{0} ".format(d))
		inpt.write("\n")
		
	inpt.close()
	
# ----
# main
# ----
"""
IMPORTANT: Run this to generate
	RunPFD.in and RunPFD.out
Then feed RunPFD.in to SpherePFD/PFD.py to get the correct RunPFD.out!
"""
n = 60
m = 50
answer = generate_output(n, m)
generate_input(n, m, answer)
