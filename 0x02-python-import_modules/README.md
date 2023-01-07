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

## Interesting questions

*What does the* <code>if __name__ == "__main__"</code> *do?*

> Before executing code, Python interpreter reads source file and define few special variables/global variables. If the python interpreter is running that module (the source file) as the main program, it sets the special __name__ variable to have a value “__main__”. If this file is being imported from another module, __name__ will be set to the module’s name. Module’s name is available as value to __name__ global variable.([GeeksForGeeks](https://www.geeksforgeeks.org/what-does-the-if-__name__-__main__-do/))
> _Example from GFG_:

```python
	print ("Always executed")
 
	if __name__ == "__main__":
    	    print ("Executed when invoked directly")
	else:
    	    print ("Executed when imported")
```

## Sidebar

Modules are a pretty powerful "utility" in Python and I cannot wait to use them! :grinning:
