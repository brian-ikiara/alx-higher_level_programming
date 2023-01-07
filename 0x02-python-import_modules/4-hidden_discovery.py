#!/usr/bin/python3
"""
    Begin:
        Import module hidden_4
        If not imported, do:
            For arguments a in hidden_4,
                If the first members characters are not "__":
                    Print a
    End
"""
import hidden_4

if __name__ == "__main__":
    for a in dir(hidden_4):
        if a[:2] != "__":
            print("{}".format(a))
