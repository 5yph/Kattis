values = list(map(int, input().split()))
order = input()

values.sort()
A = str(values[0])
B = str(values[1])
C = str(values[2])
output = []

for char in order:
    if char == "A":
        output.append(A)
    elif char == "B":
        output.append(B)
    else:
        output.append(C)

print(" ".join(output))