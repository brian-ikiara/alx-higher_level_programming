# Data Structures

## General Idea

### Lists and Tuples

```python
	#!/usr/bin/python3
	"""
	    Demonstrate the working of lists and tuples
	"""
	listDem = [1, 2, 3, 4]
	tupleDem = (5, 6, 7, 8)
	
	if __name__ == "__main__":
		listDem.append("Butter")
		listDem[1:3] = ["Dog", 0]
		listDem.pop([0])
		listDem.clear()

		# The will produce errors:
		tupleDem.pop([1])
		tupleDem.append("It's a dog")
```

## Definition of Terms

_Lists_

> Are mutable, finite, ordered data structures with elements separated by a comma and enclosed within square brackets.([Analytics Vidhya](https://www.analyticsvidhya.com/blog/2021/04/understanding-the-concept-of-list/))

_Tuples_

> Are immutable, finite, ordered data structures with elements separated by a comma and enclosed within parentheses.

## Sidebar

Data structures are essential to the functioning and implementation of a Programming Language. #pythoniscool :sunglasses:
