def sum_of_digits(number):
	""" calculates the sum of the digits of a number"""
	sum_of_digits = 0

	for digit in str(number):
		sum_of_digits += int(digit)

	return sum_of_digits

lower_bound = int(input())
upper_bound = int(input())
sum_dig = int(input())

# find integer lowest/highest integers such that its sum is 
# equal to sum_dig

# find smallest value
for i in range(lower_bound, upper_bound+1):
	if sum_of_digits(i) == sum_dig:
		lower_ans = i
		break

# find largest value
for i in range(upper_bound, lower_bound-1, -1):
	if sum_of_digits(i) == sum_dig:
		upper_ans = i
		break

print(lower_ans)
print(upper_ans)