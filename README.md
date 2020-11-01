[![PyPI version](https://badge.fury.io/py/smartswitchcase.svg)](https://pypi.org/project/smartswitchcase/)
[![PyPI version](https://img.shields.io/pypi/pyversions/smartswitchcase.svg)](https://pypi.org/project/smartswitchcase/)
[![PyPI version](https://img.shields.io/pypi/dm/smartswitchcase.svg)](https://pypi.org/project/smartswitchcase/)


[![PyPI install](https://img.shields.io/badge/Link-Install-blue.svg)](https://pypi.org/project/smartswitchcase/)
[![PyPI version](https://img.shields.io/badge/Link-GitHub-blue.svg)](https://github.com/koffiisen/smartswitchcase)
[![PyPI download](https://img.shields.io/badge/Link-Download-blue.svg)](https://pypi.org/pypi/smartswitchcase#files)

* ``BigQuery | Google cloud`` [<==>](https://cloud.google.com/bigquery/) 

[![Downloads](https://pepy.tech/badge/smartswitchcase)](https://pepy.tech/project/smartswitchcase)
[![Downloads](https://pepy.tech/badge/smartswitchcase/month)](https://pepy.tech/project/smartswitchcase/month)
[![Downloads](https://pepy.tech/badge/smartswitchcase/week)](https://pepy.tech/project/smartswitchcase/week)

### Python library of implementation of Switch Case ([SmartSwitchCase](https://github.com/koffiisen/SmartSwitchCase))

[SmartSwitchCase](https://github.com/koffiisen/SmartSwitchCase) is a simple library for use switch case statement.


## Requirements

[Python >= 2.7](https://www.python.org/downloads/) must be installed.


``Install``
------------------------------------------------------------------------------

``smartswitchcase`` is released on PyPI, so all you need is:

    $ pip install smartswitchcase

To upgrade to latest version:

    $ pip install --upgrade smartswitchcase


# Usage

### Basic Usage
```python
from smartswitchcase import SmartSwitchCase,Case

var = 2


def first():
    print("I'm ... 1")


def two():
    print("I'm ... 2")

# Initialisation
swc = SmartSwitchCase(var)
# Add case
swc.case(Case(1, first))
swc.case(Case(2, two))
# Add default statement
swc.default(lambda: "I'm ... Default")
# Run
swc.exc()

# >>> CONSOLE : I'm ... 2 <<<

```

### Advance Usage
```python
from smartswitchcase import SmartSwitchCase, Case
import random

obj = random.randint(1, 11)


def first():
    return "I'm ... 1"


def two():
    return "I'm ... 2"


# Initialisation
swc = SmartSwitchCase(obj)
# Add case
swc.case(Case(1, first))
swc.case(Case(2, two))
swc.case(Case(3, lambda: "I'm ... 3"))
swc.case(Case(4, lambda: "I'm ... 4"))
swc.case(Case(5, lambda: "I'm ... 5"))
swc.case(Case(6, lambda: "I'm ... 6"))
swc.case(Case(7, lambda: obj * 7))
swc.case(Case(8, lambda: 888))
swc.case(Case(9, lambda: 999))
# Add default statement
swc.default(lambda: "I'm ... Default")
# Run
swc.exc()
# If you statement return a result you can get her after execution
result = swc.result()
# Show the result
print(result)
```

### Advance Usage Example (LIST)
```python
from smartswitchcase import SmartSwitchCase, Case

# Initialisation
swc = SmartSwitchCase([1, 2, 3, 4, 5])
# Add case
swc.case(Case([6, 7, 8], lambda: "[6, 7, 8] Match with [1, 2, 3, 4, 5]"))
swc.case(Case([9, 10, 11], lambda: "[6, 7, 8] Match with [1, 2, 3, 4, 5]"))
swc.case(Case([1, 2, 3, 4, 5], lambda: "[1, 2, 3, 4, 5] Match with [1, 2, 3, 4, 5]"))
swc.case(Case([78, 17, 98], lambda: "[78, 17, 98] Match with [1, 2, 3, 4, 5]"))
# Add default statement
swc.default(lambda: "I'm ... Default [1, 2, 3, 4, 5]")
# Run
swc.exc()
# If you statement return a result you can get her after execution
result = swc.result()
# Show the result
print(result)
```

### Advance Usage Example (DICT)
```python
from smartswitchcase import SmartSwitchCase, Case

mydict = {
    "data": {
        "1": {"name": "Joel"},
        "2": {"name": "Github & Python"}
    }
}

# Initialisation
swc = SmartSwitchCase(mydict)
# Add case
swc.case(Case({"data": {"1": {"name": "Hi"}}}, lambda: "Maybe 1"))
swc.case(Case({"data": {"1": {"name": "Git"}, "2": {"name": "Github & Python"}, }}, lambda: "Maybe 2"))
swc.case(Case({"data": {"1": {"name": "Joel"}, "2": {"name": "Github & Python"}, }}, lambda: "Maybe 3"))
swc.case(Case({"data": {"1": {"name": "PyPi"}, "2": {"name": "Github & Python"}, }}, lambda: "Maybe 4"))
swc.case(Case({"data": {"1": {"name": "Dict"}, "2": {"name": "Github & Python"}, }}, lambda: "Maybe 5"))
# Run
swc.exc()
# If you statement return a result you can get her after execution
result = swc.result()
# Show the result
print(result)

```

Documentation
===============================================================================

#### 
* [SmartSwitchCase](smartswitchcase/smartswitchcase.py) : Take one parameter (The statement value you want tested)
* [Case](smartswitchcase/smartswitchcase.py) Take two parameters (value, func):
    - value of case
    - func is the execution function if case is match

## Project structure:

* `smartqwitchcase` - source code of a package
* `examples` - working examples

## Contribute

1. If unsure, open an issue for a discussion
1. Create a fork
1. Make your change
1. Make a pull request
1. Happy contribution!


### For support or coffee :)

[![screenshot](https://github.com/koffiisen/SmartJson/blob/master/bymecoffee.PNG?raw=true) ](https://www.paypal.me/smartjson)

## Author : [Koffi Joel ONIPOH](https://github.com/koffiisen)

