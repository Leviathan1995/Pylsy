# -*- coding: utf-8 -*-
__author__ = 'leviathan'
from  pylsy.pylsy import PylsyTable
def main():
    attributes=["name","age","sex"]
    table=PylsyTable(attributes)
    name=["sun","lsy"]
    table.AddData("name",name)
    age=[20,21]
    table.AddData("age",age)
    table.CreateTable()

if __name__ == '__main__':
    main()

