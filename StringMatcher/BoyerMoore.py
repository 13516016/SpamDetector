class BoyerMoore:
	'''String matching using BooyerMoore algorithm
		usage : 
		
		match(<string>) -> Match pattern with string. Returns True if the pattern exist in the string, otherwise return False
	 '''
	def __init__(self, pattern):
		self.pattern = pattern
		self.last_occ_table = self.__compute_last_occ()

	def get_last_occ_table(self):
		return self.last_occ_table

	def get_pattern(self):
		return self.pattern

	def __compute_last_occ(self):
		last_occ_table = dict()

		# Compute the last occurence table :
		# Each letter corresponds to the last index of the occurence within the pattern
		for idx, letter in enumerate(self.pattern):
			last_occ_table[letter] = idx

		return last_occ_table

	def match(self, string):
		pattern = self.pattern
		last_occ_table = self.last_occ_table
		pattern_end = len(pattern)-1

		i = pattern_end # string pointer
		j = pattern_end # pattern pointer

		found = False

		while(i < len(string) and not found):
			# if letters are the same, move backwards
			if (string[i] == pattern[j]):
				i-=1
				j-=1
				if (j ==-1):
					found = True
			# Otherwise, do these:
			else:
				# If the string letter is in the pattern
				if (string[i] in last_occ_table.keys()):
					# if on the left side, align the letter with the pattern
					if ( last_occ_table[string[i]] < j ):
						i += j-last_occ_table[string[i]]
					# otherwise shift pattern to align T[i+1]
					else :
						i += pattern_end
				else:
					i += len(pattern)
					
				# reset the pattern pointer to the end
				j = pattern_end
			
		return found

			

