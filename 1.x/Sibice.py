from math import sqrt

my_input = list(map(int, input().split()))
matches = my_input[0]
width = my_input[1]
height = my_input[2]
# maximum length must be diagonal distance
diagonal = sqrt(width**2+height**2)

for i in range(matches):
    match = int(input())
    if match <= diagonal:
        print("DA")
    else:
        print("NE") 
 