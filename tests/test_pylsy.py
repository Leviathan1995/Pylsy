# -*- coding: utf-8 -*-
__author__ = 'leviathan'
from pylsy import PylsyTable
def main():
    attributes=["name","age","sex","id","time"]
    table=PylsyTable(attributes)
    name=["sun","lsy","luna","leviathan"]
    table.add_data("name",name)
    age=[20,21,23,25]
    table.add_data("age",age)
    sex=["M","F","F","F"]
    table.add_data("sex",sex)
    id=[2001,2005,4242,02]
    table.add_data("id",id)
    time=["2015-8-10 11:29:54","2014-06-08 13:25:07","2014-06-0813:25:07","2014-06-08 13:25:07"]
    table.add_data("time",time)
    table.create_table()

if __name__ == '__main__':
    main()

