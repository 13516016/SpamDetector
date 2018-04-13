class BoyerMoore:
	'''String matching using BooyerMoore algorithm
		usage : 
		
		match(<string>) -> Match pattern with string. Returns True if the pattern exist in the string, otherwise return False
	 '''
	def __init__(self, pattern):
		self.pattern = pattern