#  Pylsy

[![Build Status](https://travis-ci.org/Leviathan1995/Pylsy.svg?branch=master)](https://travis-ci.org/Leviathan1995/Pylsy)

Pylsy is a simple Python library for drawing tables in the terminal/console. Just two lines of code! 

 ![image](https://raw.githubusercontent.com/Leviathan1995/Pylsy/master/pzi/span.png)
 

<h2>Install</h2>
       pip install pylsy

<h2>Sample Usage</h2>
<h6>At the very first start, pylsy needs to be imported</h6>
       from pylsy import pylsytable
<h6>First, you need to create a list, which will contain the table attributes</h6>
       attributes=["name","age","sex","id","time"]
<h6>In the second step, you need to use PylsyTable to create the ASCII table </h6>
       table=PylsyTable(attributes)
<h6>Then, you need to populate the values for each attribute and add the values to the table. Populating the values for the attribute "name" is shown below</h6>
       name=["sun","lsy","luna","leviathan"]
<h6>Then, add the values to the table </h6>
       table.add_data("name",name)
<h6>After populating each attribute and adding the values to the table, you can create the ASCII table</h6>
       print(table)

<h2>License</h2>
       MIT




