# Modules in Python

## General Idea

```python
	#!/usr/bin/python3
	"""
	    Imports function fibo that is contained in the module fibonacci
	    as fib, then prints out the result based on the value of n.
	"""
	from fibonacci import fibo as fib

	n = eval(input("Enter a number: "))

	if __name__ == "__main__":
	    print("The Fibonacci series from 1 to {:d} is {}".format(n, fib(n)))
```

## Definition of Terms

_Module_

> A Python module is a file containing Python definitions and statements. A module can define functions, classes, and variables. A module can also include runnable code. Grouping related code into a module makes the code easier to understand and use. It also makes the code logically organized.([GeeksForGeeks](https://www.geeksforgeeks.org/python-modules/))

_Commandline Arguments_

> Command line arguments are specific information passed to the program when it is started. For example, if the program needs to output data to a file, you can pass it as a command line argument instead of hardcoding it. A program can have one or more command-line arguments.([Python GUI](https://pythongui.org/what-are-command-line-arguments-and-how-to-pass-arguments-to-a-python-script/))

## Sidebar

Modules are a pretty powerful "utility" in Python and I cannot wait to use them! :grinning:
