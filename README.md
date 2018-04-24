Pylsy
=====

[![Build Status](https://travis-ci.org/Leviathan1995/Pylsy.svg?branch=master)](https://travis-ci.org/Leviathan1995/Pylsy)
[![PyPI version](https://badge.fury.io/py/Pylsy.svg)](https://badge.fury.io/py/Pylsy)

Pylsy is a simple Python library for drawing tables in the terminal/console. Just two lines of code! 

![Screenshot](https://raw.githubusercontent.com/Leviathan1995/Pylsy/master/pzi/span.png)
 
Install
-------

    pip3 install pylsy

Sample Usage
------------

```python
# In the very first, pylsy needs to be imported
from pylsy import pylsytable

# First, you need to create a list, which will contain the table attributes:
attributes=["name","age","sex","id","time"]

# Then feed it to PylsyTable to create the table object:
table=pylsytable(attributes)

# Now populate the attributes with values. Prepare a list for the names:
name=["sun","lsy","luna"]

# Add the data into it:
table.add_data("name",name)

# If you want to insert some extra values to the same column,
# you can pass a list as a parameter:
table.append_data("name",["leviathan"])

# Just a single value is OK too:
table.append_data("name",u"小明") # Note: everything will be coerced to unicode strings.

# Now with all your attributes and values, we can create our table:
print(table)

# With Python 2 things are a bit trickier, since str() is ascii-only and our dear 小明 requires unicode:
print(table.__str__()) # The raw unicode-enabled string. Think as `table.__unicode__()`.
```

License
-------
MIT
