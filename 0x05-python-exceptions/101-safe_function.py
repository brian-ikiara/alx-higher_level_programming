#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        ret = fct(*args)
        return ret
    except Exception as e:
        print("Exception: {}".format(sys.exec_info()[1]), file=sys.stderr)
        return None
