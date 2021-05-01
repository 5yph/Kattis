questions = int(input())
count = 0

for i in range(questions):
	if i == 0:
		prev_ans = input()
	else:
		ans = input()
		if ans == prev_ans:
			count += 1
		prev_ans = ans

print(count)