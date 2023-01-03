# Hello, World!

## General Idea

```python
	#!/usr/bin/python3

	import pycodestyle as pcs

	a = "Hello, World!"
	print("{}".format(a))

	checker = pcs.Checker('hello.py', show_source=True)
	errors = checker.check_all()

	print("Found {} errors".format(errors))
```

## Sidebar

"Here we go again!" - CJ, GTA San Andreas :tada:
