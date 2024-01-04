#!/usr/bin/python3
import add_0 as add_mod

# Wrapper function to intercept arguments
def wrapper_add(a, b):
    add_mod.wrap_a = a
    add_mod.wrap_b = b
    res_fun = add_mod.add(a, b)
    return res_fun

result = wrapper_add(1, 2)

a_val = add_mod.wrap_a
b_val = add_mod.wrap_b

print("{} + {} = {}".format(a_val, b_val, result))
