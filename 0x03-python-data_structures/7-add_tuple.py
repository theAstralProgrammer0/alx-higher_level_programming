#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_a = len(tuple_a)
    len_b = len(tuple_b)
    result = ()
    if len_a > len_b:
        diff = len_a - len_b
        t_b = tuple_b + (0,) * diff
    else:
        t_b = tuple_b
    if len_b > len_a:
        diff = len_b - len_a
        t_a = tuple_a + (0,) * diff
    else:
        t_a = tuple_a

    for i in range(len(t_a)):
        result += tuple([t_a[i] + t_b[i]])
    return result
