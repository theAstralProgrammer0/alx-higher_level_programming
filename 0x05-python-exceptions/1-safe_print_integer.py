#!/usr/bin/python3
def safe_print_integer(value):
    printed = False

    try:
        print("{:d}".format(value))
    except (TypeError, ValueError):
        pass
    else:
        printed = not printed 
    finally:
        return (printed)
