#!/usr/bin/python3
import sys
if __name__ == "__main__":
    count = len(sys.argv) - 1
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
        print("{}: {}".format(count, sys.argv[1]))
    else:
        print("{} arguments:".format(count))
        for i in range (1, count + 1):
            print("{}: {}".format(i, sys.argv[i]))
