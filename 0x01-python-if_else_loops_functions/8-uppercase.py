#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        print(chr(ord(ch) - 32) if (97 <= ord(ch) <= 122) else ch, end="")
    print()
