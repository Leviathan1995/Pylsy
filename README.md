#  Pylsy

Pylsy is a simple Python library designed to make it quick and easy to represent tabular data in visually appealing ASCII tables

 ![image](https://github.com/Leviathan1995/Pylsy/raw/master/span.png)
 

<h2>Install</h2>
          pip install pylsy

<h2>Sample Usage</h2>
<h6>First,you need create a list,the list include the table attributes</h6>
       attributes=["name","age","sex","id","time"]
<h6>The second step,you need use PylsyTable to create the ASCII table </h6>
       table=PylsyTable(attributes)
<h6>Then,you need create a list,the list includes the value of an attribtue</h6>
       name=["sun","lsy","luna","leviathan"]
<h6>Finally,you need to add values to the table </h6>
       table.AddData("name",name)
<h6>Now,you can create the ASCII table</h6>
       table.CreateTable()
           
<h2>License</h2>
    MIT




