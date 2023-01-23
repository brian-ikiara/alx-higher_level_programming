#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            print("{:d}".format(my_list[i]), end="")
        return i + 1
    except IndexError:
        return i
    except UnboundLocalError:
        return i
    finally:
        print()
