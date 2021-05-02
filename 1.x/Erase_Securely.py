swaps = int(input())
code1 = input()
code2 = input()

if swaps % 2 == 0:
	same = True
else:
	same = False

failed = False

for i in range(len(code1)):
	if same:
		if code1[i] != code2[i]: # not same
			print("Deletion failed")
			failed = True
			break
	if not same:
		if code1[i] == code2[i]:
			print("Deletion failed")
			failed = True
			break

if not failed:
	print("Deletion succeeded")