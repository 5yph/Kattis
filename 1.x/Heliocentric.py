flag = True
case_count = 1

while flag:
    try:
        orbits = list(map(int, input().split()))
        count = 0
        start = False
        while not start:
            if (orbits[0] % 365 == 0) and (orbits[1] % 687 == 0):
                start = True
            else:
                count += 1
                orbits[0] += 1
                orbits[1] += 1
                
        print("Case {}: {}" .format(case_count, count))
        case_count += 1
    
    except EOFError:
        flag = False
