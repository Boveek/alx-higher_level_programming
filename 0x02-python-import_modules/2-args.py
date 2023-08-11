#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv) - 1
    if argc == 0:
        print("0 arguments")
    elif argc == 1:
        print("1 argument:")
        print(f"{argc}: {sys.argv[1]}")
    elif argc > 1:
        print(f"{argc} arguments:")
        for i in range(1, argc + 1):
            print(f"{i}: {sys.argv[i]}")
