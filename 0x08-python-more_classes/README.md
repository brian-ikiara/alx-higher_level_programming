# More Classes in Python

## General Idea

```python
	vagrant@ubuntu-focal:~/0x08$ cat jacob_zuma.py
	#!/usr/bin/python3
	"""Program that demonstrates Class & Static methods.
	
	We'll be making use of the `@classmethod` and `@staticmethod`
	decorators.
	Class methods are functions within a class that directly reference
	class attributes and we'll be seeing how this is done while Static
	methods are those which don't reference either instance or class
	attributes. Phew! XD

	"""


	class JacobZuma:
		"""Represents the one and only Jacob Zuma.

		Args:
			ging (int): Beginnings

		"""

		ging = 1

		@staticmethod
		def benin():
			"""Print whatever the user wants to follow `in_de`."""
			print("beninging!")

		@classmethod
		def jayZed(cls):
			"""Print `In the beninging` ging times."""
			for i in range(cls.ging):
				print("In the", end=' ')
				cls.benin()
			cls.ging += 1
	vagrant@ubuntu-focal:~/0x08$ python3
	Python 3.8.10 (default, Nov 14 2022, 12:59:47)
	[GCC 9.4.0] on linux
	Type "help", "copyright", "credits" or "license" for more information.
	>>> JacobZuma = __import__('jacob_zuma').JacobZuma
	>>> jayZ = JacobZuma()
	>>> jayZ.jayZed.__str__
	<method-wrapper '__str__' of method object at 0x7f3fed128640>
	>>> jayZ.jayZed.__repr__
	<method-wrapper '__str__' of method object at 0x7f3fed128640>
	>>> jayZ.jayZed()
	In the beninging!
	>>> jayZ.jayZed()
	In the beninging!
	In the beninging!
	>>> jayZ.jayZed()
	In the beninging!
	In the beninging!
	In the beninging!
	>>> jayZ.jayZed()
	In the beninging!
	In the beninging!
	In the beninging!
	In the beninging!
	>>> 
	vagrant@ubuntu-focal:~/0x08$
```

## Sidebar

What we've learnt here is enough to subdue the monster that is **Inheritance**! :cold_sweat:

We'll push through anyway. :sunglasses:
