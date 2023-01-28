# TDD(Test Driven Development)

## Definition of Terms

***Testing***

> This is the process of evaluating a system or it's component(s) with the intent of finding out whether, or not, it satisfied the requirements specified. It's outlining the system's flaws, aiming to correct them once sniffed out.

***SDLC(Software Development Life Cycle)***

> It's a big picture breakdown of all the steps involved in the process of software creation.([phoenixNAP](https://phoenixnap.com/blog/software-development-life-cycle)) It entails the following phases:

| Phase | Purpose | Key Personnel | Output |
| -- | -- | -- | -- |
| Requirements Analysis | Create the overview of the project and outline the requirements of the project | Business Analysts | An SRS(*Software Requirements Specification*) document that defines project goals and needs |
| Feasibility Study | Evaluate how realistic and attainable the goals defined in the SRSDoc are | Team Leads and Higher Management | Expanded SRSDoc approved by decision maker |
| Design Plan | Generate an idea on how the product will be | Architects and Senior Developers | A detailed SDS(*Software Design Specification*) or DDS(*Design Document Specification*) document that defines how to code the product |
| Software Development | Translate the system design into source code and build the prototype | Developers | Testable, fully functional software |
| Software Testing | Ensure the product is bug & exploit free | All levels of testers | A thoroughly tested prototype |
| Software Deployment | Make the product market-ready | Deployment Engineers | Release of a fully functional and tested product |
| Maintenance | Keep the product safe and at optimal performance and continuously updating the product | Production Support Engineers, Testers & Developers | A fully monitored product that's continuously improved |

## General Idea

```python
	vagrant@ubuntu-focal:~/0x07$ cat add.py
	#!/usr/bin/python3
	"""Demonstrates TDD on an addition function.
	
	Example:
	    >>> add(6, 9)
	    15
	"""


	def add(a, b):
	    """Add two integers.

	    Args:
	        a (int): First integer
		b (int): Second integer

	    Example:
		>>> [add(x, x) for x in range(6)]
		[0, 2, 4, 6, 8, 10]
		>>> add(1, 2)
		3
		>>> add(3, 'a')
		Traceback (most recent call last):
		    ...
		TypeError: unsupported operand type(s) for +: 'int' and 'str' 
		>>> add(3, -1)
		2
		>>> add(6, 9.0)
		15.0
		>>> add(9.5, 7.5)
		17.0
	    """
	    return a + b
	
	
	if __name__ == "__main__":
	    import doctest
	    doctest.testmod()
	vagrant@ubuntu-focal:~/0x07$ python add.py -v
	Trying:
	    add(6, 9)
	Expecting:
	    15
	ok
	Trying:
	    [add(x, x) for x in range(6)]
	Expecting:
	    [0, 2, 4, 6, 8, 10]
	ok
	Trying:
	    add(1, 2)
	Expecting:
	    3
	ok
	Trying:
	    add(3, 'a')
	Expecting:
	    Traceback (most recent call last):
	        ...
	    TypeError: unsupported operand type(s) for +: 'int' and 'str'
	ok
	Trying:
	    add(3, -1)
	Expecting:
	    2
	ok
	Trying:
    	    add(6, 9.0)
	Expecting:
	    15.0
	ok
	Trying:
	    add(9.5, 7.5)
	Expecting:
    	    17.0
	ok
	2 items passed all tests:
   	    1 tests in __main__
	    6 tests in __main__.add
	7 tests in 2 items.
	7 passed and 0 failed.
	Test passed.
	vagrant@ubuntu-focal:~/0x07$
```

## "Wise sage, why is this important?"

As a Software Engineer, one's ability to develop robust and efficient code is seen through the various tests their code is put through.

*"Code that is not tested can't be trusted" - Gillaume Salva, CTO Holberton*

## What does this kind of testing entail?

You should have 3 things on your mind whilst conducting TDD:

***TP(Test Plan)***

> This outlines the strategy you'll employ, the resources you'll use, the environment you'll be carrying out the test & the limitations encountered when carrying out a test on your program. This will be carried out by the QA(Quality Assuarance) team. It includes the following:

***TS(Test Scenario)***

> It's a one-liner that outlines (an) area(s) in the program that will be tested. They ensure end-to-end testing of process flows. One can see that an area of the program may have as little as one to a few hundred TS(s).[^1]

***TC(Test Case)***

> It's a set of steps, conditions or inputs that can be used while performing testing tasks. Can be of different types: *functional*, *negative*, *error*, *logical*, *physical*, *UI* e.t.c. Written with the aim of keeping track of the testing coverage of the software.

[^1]: TS and TC may be used interchangeably, however a TS may contain several steps while the TC only has a single step.

## Honestly, how many kinds of tests can I put my code through?

Let's view this in a table:

| Testing paradigm | Area of focus | Description |
| -- | -- | -- |
| Basic | *Quality model*, *External metrics*, *Intenal metrics*, *Use quality* | Focuses on the general functionality of the program. |
| Functional | *System compliance* vs *Program's requirements* | Also referred to as *Black Box* testing; It's where the program's functionality, creation of test data, writing of TSs and execution of TCs, evaluation of the program's output, comparison of the actual with the expected results happens. |
| Unit | *Sectioning of the program* | Performed by the developers on the individual components of the program's source code before the setup is handed over to the testing team who will formally execute the test cases. |
| Integration | *Bottom-up integration*, *Top-down integration* | Combined parts of the program are tested as a whole to see how the different components interact with each other. |
| System | *Software architecture*, *Real World feasibility* | Where the program is rigorously tested as a whole checking whether it meets the QS(*Quality Standards*) |
| Regression | *Compound effect of updates* | Verifies whether debugging might have affected other components in the system |
| Acceptance | *Client satisfaction*, *Publicity* | Checks whether the Client's specifications have been met and the likelihood of the product getting embraced by the public |
| Alpha | *Typos*, *LowSpec performance*, *Algorithm* | First stage of testing that combines Unit, Integration and System testing |
| Beta | *General Performance*, *Market readiness* | A.K.A *Pre-release testing*; Where a sample of the intended audience is given a demo/beta of the product to run tests on it |
| Non-functional | *Performance*[^2], *Load*[^3], *Stress*[^4] | Also known as *White box* testing; this is the evaluation of the system's non-functional attributes such as *security*[^5], *UI & usability*[^6], *portability* e.t.c.[^7] |

[^2]: Performance testing is considered mandatory and it involves the following metrics: *Speed*, *Capacity*, *Stability* and *Scalability*
[^3]: Load testing checks the system's performance against a large sum of data & software access
[^4]: Stress can be in the form of randomly inaccessible ports, high CPU, Memory, server usage e.t.c
[^5]: Security in terms of the C.I.A(*Confidentiality, Integrity Availability*) InfoSec Triad
[^6]: UI testing is considered a subpart of Usability testing
[^7]: j = sqrt(-1)

## Sidebar

Basically, we'll be implementing our own Checker; this will be sehr intressant! :grinning:
