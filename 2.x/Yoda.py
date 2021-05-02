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

output1 = code1
output2 = code2

for i in range(length):
	# all codes should be equal now
	if int(code1[i]) < int(code2[i]):
		output1 = output1.replace(code1[i], '', 1)
		# remove 1 instance of that integer
	elif int(code2[i]) < int(code1[i]):
		output2 = output2.replace(code2[i], '', 1)

# check for leading zeroes
leading_zeroes = True
index = 0
length = len(output1)
formatted_output1 = output1

while(leading_zeroes and index < length-1):
	if output1[index] == '0':
		formatted_output1 = formatted_output1.replace(output1[index], '', 1)
		index += 1
	else:
		leading_zeroes = False

leading_zeroes = True
index = 0
length = len(output2)
formatted_output2 = output2

while(leading_zeroes and index < length-1):
	if output2[index] == '0':
		formatted_output2 = formatted_output2.replace(output1[index], '', 1)
		index += 1
	else:
		leading_zeroes = False

if len(formatted_output1) == 0:
	print("YODA")
else:
	print(formatted_output1)

if len(formatted_output2) == 0:
	print("YODA")
else:
	print(formatted_output2)