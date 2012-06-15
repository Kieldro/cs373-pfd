#!/usr/bin/env python

# -------
# imports
# -------

import StringIO
import unittest

import PFD

# -----------
# TestCollatz
# -----------

class TestPFD (unittest.TestCase) :
    # ----
    # read
    # ----

	def test_read (self) :
		r = StringIO.StringIO("5 1\n3 1 2\n")
		v = PFD.read(r)
		self.assert_(len(v) == 5)
		self.assert_(v[3-1].dependents == [2])
		
	def test_read_2 (self) :
		r = StringIO.StringIO("7 2\n5 3 1 2 3\n3 1 4\n")
		v = PFD.read(r)
		self.assert_(len(v) == 7)
		self.assert_(v[1-1].dependents == [])
		self.assert_(v[5-1].dependents == [1, 2, 3])
		self.assert_(v[3-1].dependents == [4])
		
	def test_read_3 (self) :
		r = StringIO.StringIO("100 2\n14 10 1 2 3 4 5 6 7 8 9 10\n2 1 76\n")
		v = PFD.read(r)
		self.assert_(len(v) == 100)
		self.assert_(v[99-1].dependents == [])
		self.assert_(v[14-1].dependents == range(1,11))
		self.assert_(v[2-1].dependents == [76])
	

# ----
# main
# ----

print "TestPFD.py"
unittest.main()
print "Done."
