import sys
import random

w = sys.stdout

n = 100
m = 50

print n, m

unused = range(1, n)

while m > 0 :
	# pick random vertex for rule
	r = random.choice(unused)
	unused.remove(r)

	# pick amount of rules (1-3)
	num = random.randrange(1,4)

	# pick dependent vertices
	dependent = []
	for x in range(num) :
		v = random.choice(unused)
		unused.remove(v)
		dependent += [v]

	w.write(str(r) + " ")
	for d in dependent :
		w.write(str(d) + " ")
	w.write("\n")

	m -= 1