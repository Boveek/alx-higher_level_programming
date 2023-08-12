#!/usr/bin/python3

if __name__ == "__main__":
    """Function to handle basic operator"""

    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    my_opr = {"+": add, "-": sub, "*": mul, "/": div}

    if sys.argv[2] not in list(my_opr.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        if sys.argv[2] == '+':
            print('{:d} + {:d} = {:d}'.format(a, b, add(a, b)))
        elif sys.argv[2] == '-':
            print('{:d} - {:d} = {:d}'.format(a, b, sub(a, b)))
        elif sys.argv[2] == '*':
            print('{:d} * {:d} = {:d}'.format(a, b, mul(a, b)))
        elif sys.argv[2] == "/":
            print('{:d} / {:d} = {:d}'.format(a, b, div(a, b)))
