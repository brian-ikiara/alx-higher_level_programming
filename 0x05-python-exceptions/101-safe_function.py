#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        ret = fct(*args)
    except Exception as e:
        sys.stderr.write("Exception: {}".format(e))
        ret = None
    return ret
