#!/usr/bin/python3
def subza(idx):
    res = 0
    max_idx = max(idx)

    for i in idx:
        if max_idx > i:
            res += i
    return (max_idx - res)


def roman_to_int(roman_string):
    if not roman_string:
        return 0
    if not isinstance(roman_string, str):
        return 0
    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    keys = list(romans.keys())

    num = 0
    last = 0
    idx = [0]

    for ch in roman_string:
        for r in keys:
            if romans.get(ch) <= last:
                num += subza(idx)
                idx = [romans.get(ch)]
            else:
                idx.append(romans.get(ch))
            last = romans.get(ch)
    num += subza(idx)

    return num
