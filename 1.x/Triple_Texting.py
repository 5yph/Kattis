code = input()
word_length = int(len(code)/3)

sample1 = code[:word_length]
sample2 = code[word_length:len(code)-word_length]
sample3 = code[word_length*2:]

if sample1 == sample2 or sample1 == sample3:
	# check for equality, at least 2 are equal
	print(sample1)
else:
	print(sample2)