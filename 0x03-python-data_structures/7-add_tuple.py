#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    #(1, 3) + (9, 6) = (10, 9)
    result = ()
    if len(tuple_a) == 0:
        t_a = tuple_a + (0, 0)
    elif len(tuple_a) == 1:
        t_a_p = list(tuple_a)
        t_a_p.append(0)
        t_a = tuple(t_a_p_l)
    else:
        t_a = tuple_a

    if len(tuple_b) == 1:
        t_b_p = list(tuple_b)
        t_b_p.append(0)
        t_b = tuple(t_b_p)
    elif len(tuple_b) == 0:
        t_b = tuple_b + (0, 0)
    else:
        t_b = tuple_b

    for i, j in range(2), range(2):
        return result + tuple([t_a[i] + t_b[i]]) + tuple([t_a[j] + t_b[j]])
