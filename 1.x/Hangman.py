word = list(input())
order = input()
count = 10 # hangman parts
win = True

for char in order:
	if word.count(char) == 0:
		# hangman word doesn't contain that letter
		count -= 1
	else:
		for i in range(word.count(char)):
			word.remove(char)
			# remove every instance of that char
		if len(word) == 0:
			break;

	if count == 0:
		win = False
		break

if win:
	print("WIN")
else:
	print("LOSE")