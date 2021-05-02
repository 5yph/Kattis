def remove_indices(indices, string):
	""" removes from any string all chars
	at specific indices """

	offset = 0
	# when we remove indices in order, the
	# higher indices become 1 lower
	for i in indices:
		string = string[:i+offset] + string[i+1+offset:]
		offset -= 1

	return string


def remove_leading_zeroes(string):
	""" removes all leading zeroes from an integer-like string"""
	leading_zeroes = True
	index = 0
	final_string = string

	while(leading_zeroes and index < len(string)-1):
		if string[index] == '0':
			final_string = final_string.replace(string[index], '', 1)
			index += 1
		else:
			leading_zeroes = False # no more leading zeroes, break

	return final_string

code1 = input()
code2 = input()

code1_shorter = False
code2_shorter = False

if len(code1) < len(code2):
	length = len(code2)
	code1_shorter = True
elif len(code1) > len(code2):
	length = len(code1)
	code2_shorter = True
else:
	length = len(code1)

# add leading zeroes to shorter codes
if code1_shorter:
	for i in range(len(code2) - len(code1)):
		code1 = '0' + code1
elif code2_shorter:
	for i in range(len(code1) - len(code2)):
		code2 = '0' + code2

code1_to_remove = []
code2_to_remove = []
# Record which indices need to be removed
for i in range(length):
	# all codes should be equal length
	if int(code1[i]) < int(code2[i]):
		code1_to_remove.append(i)
	elif int(code2[i]) < int(code1[i]):
		code2_to_remove.append(i)

output1 = remove_indices(code1_to_remove, code1)
output2 = remove_indices(code2_to_remove, code2)

# check for leading zeroes
formatted_output1 = remove_leading_zeroes(output1)
formatted_output2 = remove_leading_zeroes(output2)

if len(formatted_output1) == 0:
	print("YODA")
else:
	print(formatted_output1)

if len(formatted_output2) == 0:
	print("YODA")
else:
	print(formatted_output2)