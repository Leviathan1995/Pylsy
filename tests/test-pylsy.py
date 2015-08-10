# -*- coding: utf-8 -*-
__author__ = 'leviathan'
import pylsy

def main():
    attributes=["name","age","sex"]
    table=pylsyTable(attributes)
    name=["sun","lsy"]
    table.AddData("name",name)
    age=[20,21]
    table.AddData("age",age)
    table.CreateTable()

if __name__ == '__main__':
    main()

