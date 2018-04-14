import sys
import unittest
from StringMatcher import BoyerMoore

class BoyerMooreTest(unittest.TestCase):

	def test_last_occ_1(self):
		matcher = BoyerMoore("TEST")
		self.assertEqual(matcher.get_last_occ_table(), {'E': 1, 'T': 3, 'S': 2})
	
	def test_last_occ_2(self):
		matcher = BoyerMoore("TEAMMAST")
		self.assertEqual(matcher.get_last_occ_table(), {'T': 7, 'E': 1, 'A': 5, 'M': 4, 'S':6})
	
	def test_last_occ_3(self):
		matcher = BoyerMoore("abacab")
		self.assertEqual(matcher.get_last_occ_table(), {'a':4,'b':5,'c':3})
	
	def test_match_1(self):
		matcher = BoyerMoore("abacab") # a : 4, b : 5, c:3
		self.assertTrue(matcher.match("abacaabadcabacabaabb"))

	def test_match_2(self):
		matcher = BoyerMoore("rithm") # a : 4, b : 5, c:3
		self.assertTrue(matcher.match("a pattern matching algorithm"))
	
	def test_match_3(self):
		matcher = BoyerMoore("rithm") # a : 4, b : 5, c:3
		self.assertFalse(matcher.match("the rythm is so effin good"))
	
	def test_match_4(self):
		matcher = BoyerMoore("baku") # a : 4, b : 5, c:3
		self.assertTrue(matcher.match("kami menggunakan kata yang terlalu baku sehingga"))



if __name__ == '__main__':
	unittest.main()
