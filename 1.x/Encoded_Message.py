from math import sqrt

tests = int(input())

for i in range(tests):
    code = input()
    rows = int(sqrt(len(code))) # Code always fits in square
    decoded = ""
    count = 0
    offset = 0

    for j in range(len(code)):
        if count == rows: # We have finished filling out a row
            offset += 1 
            count = 0   

        decoded += code[(rows-1-offset)+(rows*count)]
        count += 1

    print(decoded)
