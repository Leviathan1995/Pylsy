# -*- coding: utf-8 -*-
__author__ = 'leviathan'
from  pylsy import PylsyTable
def main():
    attributes=["name","age","sex","id","time"]
    table=PylsyTable(attributes)
    name=["sun","lsy","luna","leviathan"]
    table.AddData("name",name)
    age=[20,21,23,25]
    table.AddData("age",age)
    sex=["M","F","F","F"]
    table.AddData("sex",sex)
    id=[2001,2005,4242,02]
    table.AddData("id",id)
    time=["2015-8-10 11:29:54","2014-06-08 13:25:07","2014-06-0813:25:07","2014-06-08 13:25:07"]
    table.AddData("time",time)
    table.CreateTable()

if __name__ == '__main__':
    main()

