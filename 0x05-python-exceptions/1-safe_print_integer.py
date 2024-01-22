#!/usr/bin/python3
def safe_print_integer(value):
    printed = False

    try:
        value = int(value)
    except (TypeError, ValueError):
        pass
    else:
        print("{:d}\n".format(value), end="")
        printed = not printed
    finally:
        return (printed)
