my_input = input()
output = ""
output += my_input[0]
hyphen = False # if next char is a capital

for char in my_input:
	if char == '-':
		hyphen = True
	elif hyphen:
		output += char
		hyphen = False

print(output)