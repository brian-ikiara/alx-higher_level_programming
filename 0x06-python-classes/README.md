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

* *Class attributes*: Are variables defined within the class and are not within a method and can be used throughout the class by any object. Defined as follows: `cls.var`(*for public*) & `cls.__var`(*for private*)
* *Instance attributes*: Are variables defined within methods and can't be used by other objects in the class. Defined as follows: `self.var`(*for public*) & `self.__var`(*for private*)

[^1]: In C, we use this a lot in Linked lists and other numerous implementations.

## General Idea

```python
	#!/usr/bin/python3
	"""Demonstrates the working of a class.
	
	We'll be demonstrating how we can define our own 'data types', for
	example, we'll be defining the dog data type.

	"""


	class Doggo:
	    """Represents a real life dog."""

	    doggos = 0

	    def __init__(self, name, age):
		"""Instantiate the name, age & breed attributes.

		Args:
		    name (str): dog's name
		    age (int): dog's age

		"""
		# public instance attribute
		self.name = name
		# private instance attribute
		self.__age = age
	    
	    @property
	    def age(self):
		"""Get the dog's age.

		The '@property' is known as a decorator. it declares this
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
		    years (int): age in dog years.

		"""
		if isinstance(years, int):
		    if years < 0:
		        raise ValueError("Your dog is too young!")
		    if years > 30:
		        raise ValueError("Your dog is too old. contact guinness world records")
		    self.__age = years
		    doggos += 1
		else:
		    raise TypeError("Age should be a number")

	    def print_doggo(self):
		"""Print the Doggo's info."""
		print("This is Doggo #{:d}".format(doggos, end=" ")
		print("They're called {}".format(self.name), end=" ")
		print("and they're {:d} years old.".format(self.__age))

	if __name__ == "__main__":
	    dog1 = Doggo("Butter", 5)
	    Doggo.print_doggo()
	    dog2 = doggo("dodge", 6)
	    doggo.print_doggo()
```

## Sidebar

Will be updated later. It's a pretty big deal, bro! :sunglasses:
