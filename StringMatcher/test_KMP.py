import sys
import unittest
from StringMatcher import KMP

class KMPTest(unittest.TestCase):

	def test_border_1(self):
		matcher = KMP("AAAA")
		self.assertEqual(matcher.get_border_table(), [0, 1, 2, 3])
	
	def test_border_2(self):
		matcher = KMP("ABCDE")
		self.assertEqual(matcher.get_border_table(), [0, 0, 0, 0, 0])
	
	def test_border_3(self):
		matcher = KMP("AABAACAABAA")
		self.assertEqual(matcher.get_border_table(), [0, 1, 0, 1, 2, 0, 1, 2, 3, 4, 5])
	
	def test_border_4(self):
		matcher = KMP("AAACAAAAAC")
		self.assertEqual(matcher.get_border_table(), [0, 1, 2, 0, 1, 2, 3, 3, 3, 4])

	def test_border_5(self):
		matcher = KMP("AAABAAA")
		self.assertEqual(matcher.get_border_table(), [0, 1, 2, 0, 1, 2, 3])
	
	def test_border_6(self):
		matcher = KMP("AABAABAAA")
		self.assertEqual(matcher.get_border_table(), [0, 1, 0, 1, 2, 3, 4, 5, 2])
	
	def test_border_7(self):
		matcher = KMP("acacabacacabacacac")
		self.assertEqual(matcher.get_border_table(), [0,0,1,2,3,0,1,2,3,4,5,6,7,8,9,10,11,4])
	
	def test_border_8(self):
		matcher = KMP("abcaby")
		self.assertEqual(matcher.get_border_table(), [0,0,0,1,2,0])

	def test_match_1(self):
		matcher = KMP("abc")
		self.assertTrue(matcher.match("abcdef"))
	
	def test_match_2(self):
		matcher = KMP("abcaby")
		self.assertTrue(matcher.match("abxabcabcaby"))
	
	def test_match_3(self):
		matcher = KMP("bcgl")
		self.assertTrue(matcher.match("abcbcglx"))

	def test_match_4(self):
		matcher = KMP("bcgl")
		self.assertFalse(matcher.match("abcbcgdbclgx"))
	
	def test_match_5(self):
		matcher = KMP("checking it out")
		self.assertTrue(matcher.match("hello world! please consider checking it out!"))
	
	def test_match_6(self):
		matcher = KMP("alksjflkasjflkasjfaslfjlasjflajsflajsflasjflasjflkasjflkasjflkasjflkjsaf")
		self.assertTrue(matcher.match("09012102412sdjadalksjflkasjflkasjfaslfjlasjflajsflajsflasjflasjflkasjflkasjflkasjflkjsafm,zxcoqwo90e12ne12e"))
	
	def test_match_7(self):
		matcher = KMP("SINGLES AROUND YOU")
		self.assertTrue(matcher.match("CHECK THIS OUT! SINGLES AROUND YOU!!"))


if __name__ == '__main__':
	unittest.main()
