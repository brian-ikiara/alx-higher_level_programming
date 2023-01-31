#!/usr/bin/python3
"""Indents text passed to it."""


def text_indentation(text):
    """Indent text.

    If character in text is a member of the set {'.', '?', ':'},
    then text will be indented at that point.

    Args:
        text (str): Text.

    Raises:
        TypeError: If text is not a string.

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
