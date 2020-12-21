
def build_matrix(row1, row2):
    """ 
    Builds a matrix given its rows
    Arguments:
        Rows of the matrix (list of ints)
    Returns: List of lists representing matrix
    """
    matrix = [] # Always 2x2
    matrix.append(row1)
    matrix.append(row2)

    return matrix


def determinant(matrix):
    """ 
    Calculates the determinant of the given matrix
    Arguments:
        Matrix (list of lists)
    Returns:
        Determinant (int) of matrix.
    """
    det = (matrix[0][0]*matrix[1][1])-(matrix[0][1]*matrix[1][0])

    assert det != 0 # No inverse
    return det


def inverse(determinant, matrix):
    """
    Calculates inverse of given matrix
    Arguments:
        Matrix (list of lists)
        Determinant of matrix (int)
    Returns:
        Inverse matrix (list of lists)
    """
    coefficient = int(1/determinant)
    inverse = []
    new_row1 = []
    new_row2 = []

    # Multiply the cells by determinant inverse
    for elem in matrix[0]: # Iterate over 1st row
        new_elem = elem*coefficient
        new_row1.append(new_elem)

    for elem in matrix[1]:
        new_elem = elem*coefficient
        new_row2.append(new_elem)

    inverse.append(new_row1)
    inverse.append(new_row2)

    # Reorganize according to inverse definition
    a = inverse[0][0]
    b = inverse[0][1]
    c = inverse[1][0]
    d = inverse[1][1]

    new_inverse = []
    newer_row1 = []
    newer_row2 = []

    newer_row1.append(str(d))
    newer_row1.append(str(-b))
    newer_row2.append(str(-c))
    newer_row2.append(str(a))

    new_inverse.append(newer_row1)
    new_inverse.append(newer_row2)

    return new_inverse


def print_matrix(inverse, case):
    """
    Prints matrix
    Arguments:
        Inverse matrix (list of lists)
        Test case number(int)
    """
    print("Case {}:" .format(case))
    print(" ".join(inverse[0]))
    print(" ".join(inverse[1]))

if __name__ == "__main__":

    case = 1
    flag = True
    while flag:
        try:
            row1 = list(map(int, input().split()))
            if not row1: # Blank line detected 
                case += 1
                continue
            else:
                row2 = list(map(int, input().split()))
                matrix = build_matrix(row1, row2)
                det = determinant(matrix)
                output = inverse(det, matrix)
                print_matrix(output, case)

        except EOFError:
            flag = False
