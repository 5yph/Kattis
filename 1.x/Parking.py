tests = int(input())

for i in range(tests):
    stores = int(input())
    positions = list(map(int, input().split()))
    distance = 0
    # The optimal place to park is at the first store
    car = positions[0]
    # He makes n trips where n = # of stores
    for i in range(stores):
        if i == (stores - 1): # walks back to car
            distance += abs(positions[i] - car)
        else:
            distance += abs(positions[i] - positions[i+1])

    print(distance)
