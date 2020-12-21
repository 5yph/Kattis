from math import sqrt

N = int(input())

# Recognize in the algorithm, the number of successive squares
# is 4x the previous amount of squares.

# Recognize that the total amount of squares fits neatly into an array
# with length sqrt(total squares).

# Recognize that an array of points has one extra row and column compared
# to the array of squares.

squares = 1 # Start

for i in range(1, N+1):
    new_squares = squares * 4 # for iteration i
    squares = new_squares

squares_per_row = sqrt(squares)
points_per_row = squares_per_row + 1
total = points_per_row ** 2

print(int(total))