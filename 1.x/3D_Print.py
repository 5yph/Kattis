import math

statues = int(input())

# Recognize most efficient algorithm is printing all required
# printers at the start to maximize efficiency.

# N statues take (N/P) + Q days to print, where P is the 
# number of printers and Q is the time taken to print P printers,
# rounded up.

# Realize that we can double our printers each day at most.
# So if days = D. and 2^D = P, the log2(P) = D.

# We get D = (N/P) + log2(P). The only thing we need now is
# to figure out how many printers we should print for fastest time.

flag = True
printers = 2

while flag:
	# Takes more time to print printers
    if math.log(printers, 2) >= math.ceil(statues/(printers/2)):
        printers = printers/2
        flag = False
    else:
        printers = printers * 2 

days_for_printers = math.log(printers, 2)
total = math.ceil(statues/printers) + days_for_printers
print(int(total))