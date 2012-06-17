#!/usr/bin/env python

# -------
# imports
# -------

import StringIO
import unittest
import sys

import PFD
# -----------
# TestCollatz
# -----------

class TestPFD (unittest.TestCase) :
    # ----
    # read
    # ----

	def test_read_1 (self) :
		r = StringIO.StringIO("5 1\n3 1 2\n")
		v = PFD.read(r)
		self.assert_(len(v) == 5)
		self.assert_(v[3-1].dependents == [2])
		self.assert_(v[2-1].successors == [3])
		
	def test_read_2 (self) :
		r = StringIO.StringIO("7 2\n5 3 1 2 3\n3 1 4\n")
		v = PFD.read(r)
		self.assert_(len(v) == 7)
		self.assert_(v[1-1].dependents == [])
		self.assert_(v[5-1].dependents == [1, 2, 3])
		self.assert_(v[3-1].dependents == [4])
		self.assert_(v[1-1].successors == [5])
		self.assert_(v[2-1].successors == [5])
		self.assert_(v[3-1].successors == [5])
		self.assert_(v[4-1].successors == [3])
		
	def test_read_3 (self) :
		r = StringIO.StringIO("100 2\n14 10 1 2 3 4 5 6 7 8 9 10\n2 1 76\n")
		v = PFD.read(r)
		self.assert_(len(v) == 100)
		self.assert_(v[99-1].dependents == [])
		self.assert_(v[14-1].dependents == range(1,11))
		self.assert_(v[2-1].dependents == [76])
		self.assert_(v[1-1].successors == [14])
		self.assert_(v[2-1].successors == [14])
		self.assert_(v[3-1].successors == [14])
		self.assert_(v[4-1].successors == [14])
		self.assert_(v[5-1].successors == [14])
		self.assert_(v[6-1].successors == [14])
		self.assert_(v[7-1].successors == [14])
		self.assert_(v[8-1].successors == [14])
		self.assert_(v[9-1].successors == [14])
		self.assert_(v[10-1].successors == [14])
		self.assert_(v[76-1].successors == [2])
	
	def test_read_4 (self) :
		r = StringIO.StringIO("4 3\n1 1 2\n2 1 3\n4 1 3\n")
		v = PFD.read(r)
		self.assert_(len(v) == 4)
		self.assert_(v[1-1].dependents == [2])
		self.assert_(v[2-1].dependents == [3])
		self.assert_(v[4-1].dependents == [3])
		self.assert_(v[1-1].successors == [])
		self.assert_(v[2-1].successors == [1])
		self.assert_(v[3-1].successors == [2, 4])
		self.assert_(v[4-1].successors == [])

	# ----
	# solve
	# ----

	def test_solve_1 (self) :
		#v = [Vertex(i+1, [i]) for i in xrange(4)]
		r = StringIO.StringIO("4 3\n1 1 2\n2 1 3\n4 1 3\n")
		v = PFD.read(r)
		s = PFD.solve(v)

	def test_solve_2 (self) :
		r = StringIO.StringIO("3 2\n3 1 2\n2 1 1\n")
		v = PFD.read(r)
		s = PFD.solve(v)
		self.assert_(s == [1, 2, 3])

	def test_solve_3 (self) :
		r = StringIO.StringIO("5 3\n5 2 4 3\n4 2 3 2\n2 1 3")
		v = PFD.read(r)
		s = PFD.solve(v)
		self.assert_(s == [1, 3, 2, 4, 5])

	def test_solve_4 (self) :
		r = StringIO.StringIO("6 3\n1 1 6\n4 1 6\n5 1 3")
		v = PFD.read(r)
		s = PFD.solve(v)
		self.assert_(s == [2, 3, 5, 6, 1, 4])

	def test_solve_5 (self) :
		r = StringIO.StringIO("3 1\n1 1 2\n")
		v = PFD.read(r)
		s = PFD.solve(v)
		self.assert_(s == [2, 1, 3])

	# ----
	# output
	# ----

	def test_output_1 (self) :
		w = StringIO.StringIO()
		v = PFD.output(w, [1, 2, 3])
		self.assert_(w.getvalue() == "1 2 3 \n")

	def test_output_2 (self) :
		w = StringIO.StringIO()
		v = PFD.output(w, [1])
		self.assert_(w.getvalue() == "1 \n")

	def test_output_3 (self) :
		w = StringIO.StringIO()
		v = PFD.output(w, [1, 2, 3, 4])
		self.assert_(w.getvalue() == "1 2 3 4 \n")

# ----
# main
# ----

print "TestPFD.py"
#runner = unittest.TextTestRunner(sys.stdout)
unittest.main()#testRunner=runner)
print "Done."
