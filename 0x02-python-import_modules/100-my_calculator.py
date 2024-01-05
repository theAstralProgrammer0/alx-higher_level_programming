#!/usr/bin/python3
def main():
    length = len(sys.argv)
    if not length == 4:
        print("Usage: ./100-my_calculator.py <a> <oprterator> <b>")
        sys.exit(1)

    oprd_1 = int(sys.argv[1])
    oprt = sys.argv[2]
    oprd_2 = int(sys.argv[3])
    ops = ["+", "-", "*", "/"]

    if oprt == ops[0]:
        print("{} + {} = {}".format(oprd_1, oprd_2, add(oprd_1, oprd_2)))
    elif oprt == ops[1]:
        print("{} - {} = {}".format(oprd_1, oprd_2, sub(oprd_1, oprd_2)))
    elif oprt == ops[2]:
        print("{} * {} = {}".format(oprd_1, oprd_2, mul(oprd_1, oprd_2)))
    elif oprt == ops[3]:
        print("{} / {} = {}".format(oprd_1, oprd_2, div(oprd_1, oprd_2)))
    else:
        print("Unknown oprterator. Available operators: +, -, * and /")
        sys.exit(1)


if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    main()
