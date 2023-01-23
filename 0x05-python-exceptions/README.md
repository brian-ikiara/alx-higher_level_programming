# Exception handling in Python

## General Idea

```bash
	vagrant@ubuntu-focal:~/0x05$ python3
	Python 3.8.10 (default, Nov 14 2022, 12:59:47)
	[GCC 9.4.0] on linux
	Type "help", "copyright", "credits" or "license" for more information.
	>>> while True print("Hello, World!")
	  File "<stdin>", line 1
    	    while True print("Hello, World!")
               ^
	SyntaxError: invalid syntax
	>>> 10 * (1 / 0)
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	ZeroDivisionError: division by zero
	>>> 4 + spam*3
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	NameError: name 'spam' is not defined
	>>> '2' + 2
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	TypeError: can only concatenate str (not "int") to str
	>>> exit()
	vagrant@ubuntu-focal:~/0x05$
```

## Definition of Terms

***Errors***

> These are faults/problems that occur in the program that results in abnormal behaviour of the program. Are of 2 main types in Python:

* _Syntax errors_: These occur when a programmer fails to write the code in a manner that obeys the rules that define the structure of Python, known as the *syntax*. Are caught during **compilation**

* _Logical errors_: Also known as *exceptions*, occur when the programmer's algorithm may have a fault e.g. division by zero, undefined variables or performing operations on symbols that aren't the same type. Are caught during runtime/execution of the program. Below are some examples of Python exceptions:

(_Source_: [3.11.1 Documentation](https://docs.python.org/3/library/exceptions.html#bltin-exceptions))

| Exception | Description |
| -- | -- |
| ZeroDivisionError | Occurs when one tries to divide a number by zero |
| IndentationError | Part of Python's syntax is indentation; mess that up, you'll affect the flow of logic in function definitions, loops, conditionals e.t.c |
| IndexError | Occurs when a non-existent position is referenced in a given DS[^1] |
| NameError | Occurs when a variable is undefined |
| MemoryError | Occurs when program runs out of memory |
| EOFError | Occurs when input() receives Ctrl-D(End of File) condition |
| NotImplementedError | Occurs when an abstract method[^2] is called |
| OverflowError | Occurs when the result of an operation is too large |
| OSError | Occurs when program causes system-related problems |
| RuntimeError | Occurs when program causes a fault that is out-of-bounds of Python's exception scope |
| TabError | Occurs when indentation alternates between tabs and spaces |
| SystemError | Occurs when interpreter detects internal error |
| ValueError | Occurs when operation or function receives an arguement of the right type but an inappropriate value |

[^1]: Raised when a sequence subscript is out of range
[^2]: undefined function

## Why do I need this?

Exceptions, compared to syntax errors, are not entirely fatal and managing these errors in execution is necessary especially when one may not desire premature termination of the program. It's also necessary when testing the program and figuring out refactorization and optimization of the code.

They can be either user-defined or built-in. For the latter, we'll make use of the `try`, `except`, `raise` and `finally` keywords. Let's see this in action! :grinning:

```python
	#!/usr/bin/python3
	# Demonstrates error handling in Python
	def zero_division():
	    raise ZeroDivisionError("ooooooooooooooooooooHHHHHHHHHHHHHH!")
	
	if __name__ == "__main__":
	    errors = []

	    for i in range(69):
		try:
		    zero_division()
		except Exception as e:
		    e.add_note("Why you dividing by Zero? This is your {}".format(i + 1))
		    errors.append(e)
	        finally:
		    print("Ginuwine!")

	    raise ExceptionGroup('We gonna have a problem son!')
```

## Sidebar

Errors can be a handful, you've got to be prepared for the nasty little surprises they can bring forth from their tiny impish selves! :laughing:. This is going to be serious fun.
