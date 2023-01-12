# More on Data Structures

## General Idea

### Sets and Dictionaries

```python
	#!/usr/bin/python3

	"""
	    Sets are unordered collection of elements with no duplicates
	    The following is a set
	"""
	fruits = {banana, mango, tomato, strawberry}
	'''
            Sets automatically detect duplicate elements and exclude them
	    whenever one calls to print out the set. e.g.:
	'''
	# Set constructor set() builds a set from sequences. Don't use {}
	a, b = set('abracadabra'), set('alacazam')
	# a will be printed out as {'a', 'r', 'b', 'c', d}
	# MathOps(a.k.a Membership testing) can be performed on the sets, e.g:
	print(a - b) # Letters in a but not in b i.e. {'r', 'd', 'b'}
	print(a | b) # Letters in a or b or both(union of a & b) i.e. {'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
	print(a & b) # Letters in both a and b(intersection) i.e. {'a', 'c'}
	print(a ^ b) # Letters in a or b but not both i.e. {'r', 'd', 'b', 'm', 'z', 'l'}
	# Set comprehension is supported:
	s = {x for x in 'udenana' if x not in 'na'}
	print(s) # {'u', 'd', 'e'}

	"""
	    Dictionaries are 'associative memories/arrays'; are indexed by keys unlike
	    sequences(lists, tuples). Keys are immutable in nature so one can use either
	    strings, integers or tuples(if tuple contains a mutable type it can't be used)
	    Members exist as key-value pairs.

	    The following is a dictionary:
	"""
	d = {'one': 1, 'two': 2}
	d['three'] = 3 # Adding a member three with the value 3 to d
	print(d['one']) # Returns value 1
	del d['two'] # Removes member two and its value from the dictionary
	print(list(d)) # Prints a list of d's keys i.e. ['one', 'three']
	# Dictionary constructor dict() builds a dictionary from a sequence with key-value pairs; {} builds an emptydictionary
	new_d = dict([('apples', 34.5), ('bananas', 420), ('oranges', 69.0)])
	print(new_d) # {'apples': 34.5, 'bananas': 420, 'oranges': 69.0}
	# Dictionary comprehensions can be used to create dictionaries from arbitrary key and value expressions
	c_d = {x: x ** 2 for x in (2, 4, 6)}
	print(c_d) # {2: 4, 4: 16, 6: 36}
	# Dictionaries can be created, also, when the keys are simple strings
	ss_d = dict(simple=5, stringu=6, dicto=7)
	print(ss_d) # {'simple': 5, 'stringu': 6, 'dicto': 7}
```

### lambda, map(), filter() & reduce()

```python
	#!/usr/bin/python3
	"""
	    lambda is an operator that defines a set of anonymous functions
	    Syntax:
	    	lambda args_list: expression

	    The following functions work similarly:
	"""
	a, b = 6, 9
	def f_sum(x, y):
		return x + y
	l_sum = lambda x, y: x + y
	print(f_sum(a, b)) # 15
	print(l_sum(a, b)) # 15
	
	"""
	    map() returns a list of the application of a function to a sequence
	    Syntax:
		map(function, sequence)

	    The following work similarly:
	"""
	# Normal function definition
	def fahr(t):
	    return ((float(9) / 5) * (t + 32))
	def cels(t):
	    return ((float(5) / 9) * (t - 32))
	temp = (35, 37.5, 25, 69.69)
	F = list(map(fahr, temp))
	C = list(map(cels, F))
	print(F, C)
	# Using lambda
	lC = [69, 96, 69.96, 96. 69]
	lF = list(map(lambda x: (float(9) / 5) * (x + 32), lC))
	print(lF)
	rlC = list(map(lambda y: (float(5) / 9) * (x - 32), lF))
	print(rlC)

	"""
	    filter() returns a list containing the return values specified
	    by a function
	    Syntax:
	        filter(function, sequence)

	    Let's see this in action:
	"""
	fibo = [0,1,1,2,3,5,8,13,21,34,55]
	odd_fibo = list(filter(lambda x: x % 2, fibo))
	even_fibo = list(filter(lambda y: y % 2 == 0, fibo))
	# even_fibo can be alternatively defined as ...lambda y: y % 2 -1, fibo))
	print(odd_fibo) # [1, 1, 3, 5, 13, 21, 55]
	print(even_fibo) # [0, 2, 8, 34]
```

## Sidebar

Wueh! Just funny how even the creator of Python hates reduce() :laughing: 
