#!/usr/bin/python3
def max_integer(my_list=[]):
    maxim = 0
    if not my_list:
        return None
    for num in my_list:
        if maxim < num:
            maxim = num
    return maxim
