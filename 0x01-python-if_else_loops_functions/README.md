# Conditionals, Loops and Functions

## General Idea

### Conditionals

```python
	#!/usr/bin/python3
	
	"""
		Checks whether a number is even or odd
	"""
	a = input("Enter a number: ")

	if (a % 2) == 0:
		print(f"{a:d} is even")
	else
		print(f"{a:d} is odd")
```

### Loops

```python
	#!/usr/bin/python3
	"""
		Displays a pine tree based on user's input
	"""
	height = eval(input("How tall is the tree? "))
	spaces, hashes, stump = height - 1, 1, height - 1

	while height != 0:
		for i in range(spaces):
			print(' ', end="")
		for i in range(hashes):
			print('#', end="")
		print()
		spaces -= 1
		hashes += 2
		height -= 1
	for i in range(stump):
		print(' ', end="")
	print("#")
```

### Functions

```python
	#!/usr/bin/python3
	"""
		Returns the sum of 2 integers
	"""
	def add(a, b):
		sum = a + b
		return sum
	a, b = eval(input("Enter 2 integers: ").split())
	print(f"{a:d} + {b:d} = {add(a, b):d}")
```

## Sidebar

Python is so much fun! OMG! :laughing:
