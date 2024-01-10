#!/usr/bin/python3
my_list = [(1, 2), (2, 1), (3, 10), (4, 2)]
def weight_average(my_list=[]):
    if not my_list:
        return 0
    num = 0
    den = 0
    for tup in my_list:
        num += (tup[0] * tup[1])
        den += tup[1]
    return num / den


