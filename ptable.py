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
    def PrintDivide(self):
        for space in self.AttributesLength:
            print "+",
            for sign in range(space):
                print "-",
        print "+"
    def AddData(self,attribute,values):
        for row in self.Table:
            if row.has_key(attribute):
                row[attribute]=values
    def CreateTable(self):
        for row in self.Table:
            values=row.values()[0]
            if self.Linesnum<len(values):
                self.Linesnum=len(values)
            Len=len(row.keys()[0])
            for value in values:
                length=len(value)
                if length>Len:
                    Len=length
            self.AttributesLength.append(Len)
        self.PrintHead()
        self.PrintValue()
    def PrintHead(self):
        self.PrintDivide()
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
        self.PrintDivide()
    def PrintValue(self):
        for line in range(self.Linesnum):
            for row,length in zip(self.Table,self.AttributesLength):
                print "|",
                valuelength=length*2-1
                value=row.values()[0]
                if len(value)!=0:
                    start=(valuelength-len(value[line]))/2
                    for space in range(start):
                        print "",
                    print value[line],
                    end=valuelength-start-len(value[line])
                    for space in range(end):
                        print "",
                else:
                    start=0
                    end=valuelength-start+1
                    for sapce in range(end):
                        print "",
            print "|"
            self.PrintDivide()









def main():
    table=Ptable(["name","age","sex","hobby"])
    table.AddData("name",["sun","liu"])
    table.CreateTable()


if __name__=='__main__':
    main()