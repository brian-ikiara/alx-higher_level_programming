# Classes in Python

## Definition of Terms

***Class***

> Can be defined as a blueprint for constructing objects. Just think of it as an advanced form of `struct`[^1].

***Object***

> It's an *instance* of a class i.e. as the class is a blueprint, an instance is the copy that contains values to be used. It usually consists of the following:

* *Identity*: Unique name of the object that allows interaction between objects
* *State*: Represented by the attributes of an object. Reflects the properties of the object
* *Behaviour*: Represented by the methods of an object. Reflects the object's interaction with other objects

***Method***

> A funtion defined within the class.

***Attributes***

> Instance variables defined within the class. Are of two main types:

* *Class attributes*: Are variables defined within the class and are not within a method and can be used throughout the class by any object
* *Instance attributes*: Are variables defined within methods and can't be used by other objects in the class.

[^1]: In C, we use this a lot in Linked lists and other numerous implementations.

## General Idea

```python
	#!/usr/bin/python3
	"""Demonstrates the working of a class.
	
	We'll be demonstrating how we can define our own 'data types', for
	example, we'll be defining the Dog data type.

	"""


	class Doggo:
	    """Represents a real life dog."""

	    dog_count = 0

	    def __init__(self, name, age):
		"""Instantiate the name, age & breed attributes.

		Args:
		    name (str): Dog's name
		    age (int): Dog's age

		"""
		# Public instance attribute
		self.name = name
		# Private instance attribute
		self.__age = age
	    
	    @property
	    def age(self):
		"""Get the dog's age.

		The '@property' is known as a decorator. It declares this
		method as a getter function. Utilized by private instance
		attributes when a specific value is required.

		"""
		return self.__age
	    
	    @age.setter
	    def age(self, years):
		"""Set the dog's age.
		
		The '@age.setter' declares this method as a setter function,
		it's a decorator too. Assigns a value to the private instance
		attribute that meets the criteria specified here.

		Args:
		    years (int): Age in Dog years.

		"""
		if isinstance(years, int):
		    if years < 0:
		        raise ValueError("Your dog is too young!")
		    if years > 30:
		        raise ValueError("Your dog is too old. Contact Guinness World Records")
		    self.__age = years
		    dog_count += 1
		else:
		    raise TypeError("Age should be a number")

	    def print_doggo(self):
		"""Print the dog(s) info."""
		if dog_count > 0:
		    for i in range(dog_count + 1):
		    	print("This is Dog #{:d}. The dog's name is {} and they're {:d} years old".format(i, self.name, self.__age))

```

## Sidebar

Will be updated later. It's a pretty big deal, bro! :sunglasses:
