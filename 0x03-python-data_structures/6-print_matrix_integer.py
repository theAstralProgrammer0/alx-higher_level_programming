#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print("{}".format('\n'), end="")
    else:
        for i in range(len(matrix)):
            for j in range(len(matrixi[i])):
                if j != 2:
                    print("{:d} ".format(matrix[i][j]), end="")
                else:
                    print("{:d}".format(matrix[i][j]), end="")
            print("{}".format('\n'), end="")
