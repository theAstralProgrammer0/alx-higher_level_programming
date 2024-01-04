#!/usr/bin/python3
for ch_a in range(122, 96, -1):
    # if ascii value is odd
    print(chr(ch_a) if not ch_a % 2 else chr(ch_a - 32), end="")
