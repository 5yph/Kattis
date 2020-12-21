values = input().split()
order = input()

values.sort()
A = values[0]
B = values[1]
C = values[2]
output = []

for char in order:
    if char == "A":
        output.append(A)
    elif char == "B":
        output.append(B)
    else:
        output.append(C)

print(" ".join(output))