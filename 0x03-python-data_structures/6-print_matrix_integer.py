#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print("{}".format('\n'), end="")
    else:
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if j != 2:
                    print("{} ".format(matrix[i][j]), end="")
                else:
                    print("{}".format(matrix[i][j]), end="")
            print("{}".format('\n'), end="")
