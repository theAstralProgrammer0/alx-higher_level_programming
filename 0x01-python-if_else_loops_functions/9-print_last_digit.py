#!/usr/bin/python3
def print_last_digit(number):
    last_digit = str(number)[len(str(number)) - 1]
    print(f"{last_digit}", end="")
    return (last_digit)
