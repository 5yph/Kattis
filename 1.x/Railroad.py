my_list = list(map(int, input().split()))
junctions = my_list[0]
switch = my_list[1]

# Recognize that each junction has 4 ends, each switch has 3
# Recognize that total ends must be even to be closed

ends = 4 * junctions + 3 * switch
if ends % 2 == 0:
    print("possible")
else:
    print("impossible")