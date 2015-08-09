# -*- coding: utf-8 -*-
class Ptable:
    def __init__(self,attributes):
        self.Attributes=attributes
        self.Table=[]
        self.AttributesLength=[]
        self.Rowsnum=len(self.Attributes)
        self.Linesnum=0
        for attribute in self.Attributes:
            row=dict()
            row[attribute]=""
            self.Table.append(row)
    def AddData(self,attribute,values):
        for row in self.Table:
            if row.has_key(attribute):
                row[attribute]=values
    def CreateTable(self):
        for row in self.Table:
            values=row.values()
            Len=len(row.keys()[0])
            for value in values:
                for item in value:
                    length=len(item)
                    if length>Len:
                        Len=length
                self.AttributesLength.append(Len)
        self.PrintHead()
    def PrintHead(self):
        for space in self.AttributesLength:
            print "+",
            for sign in range(space):
                print "-",
        print "+"
        print "|",
        for spaces,attr in zip(self.AttributesLength,self.Attributes):
            spacenum=spaces*2-1
            start=(spacenum-len(attr))/2
            for space in range(start):
                print "",
            print attr,
            end=spacenum-start-len(attr)
            for space in range(end):
                print "",
            print "|",
        print ""
        for space in self.AttributesLength:
            print "+",
            for sign in range(space):
                print "-",
        print "+"







def main():
    table=Ptable(["name","age","sex","hobby"])
    table.AddData("name",["sun","liu"])
    table.CreateTable()


if __name__=='__main__':
    main()