class KMP:
	'''String matching using KMP algorithm
		
		usage : 

		get_border() -> Returns the border function array
		match(<string>) -> Match pattern with string. Returns True if the pattern exist in the string, otherwise return False

	 '''
	def __init__(self, pattern):
		self.pattern = pattern
		self.border = self.__compute_borders()

	def get_border_table(self):
		return self.border;
	
	def get_pattern(self):
		return self.pattern;

	def __compute_borders(self):
		border = [0]
		i = 1
		j = 0

		prefix_count = 0
		pattern = self.get_pattern()

		while(i < len(self.pattern)):
			# If pattern[i] == pattern[j] : add prefix count and increment i and j
			if (pattern[j] == pattern[i]):
				prefix_count = j+1
				j+=1
			else: 
			# If pattern[i] =/= pattern[j] :  search for the longest substring that is a prefix
				while(j > 0 and pattern[j] != pattern[i]):
					j = border[j-1]
					prefix_count = j

				if (pattern[j] == pattern[i]):
					prefix_count += 1

			border.append(prefix_count)
			i+=1
		
		return border

	def match(self, string):
		found = False
		i = 0
		j = 0

		pattern = self.get_pattern()
		border_table = self.get_border_table()
		while(i < len(string) and not found):
			# if string[i] =/= pattern[j] : jump to the index of the border[j-1] (latest index of passed prefix)
			if (string[i] != pattern[j]):
				if (j > 0):
					j = border_table[j-1]
			# if string[i] == pattern[j] : increment j (continue reading the next character)
			if (string[i] == pattern[j]):
				j+=1

			if (j == len(pattern)):
				found = True

			i+=1

		return found
