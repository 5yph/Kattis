tests = int(input())

for i in range(tests):
    temp_list = list(map(int, input().split()))
    x, y, z = temp_list[0], temp_list[1], temp_list[2]
    # Since addition/multiplication are inverses of subtraction/multiplication,
    # we really only need to test one of these cases
    # We test addition/multiplication because they are commutative.

    if (x + y == z) or (x + z == y) or (x*y == z) or (x*z == y):
        print("Possible")
    else:
        print("Impossible")