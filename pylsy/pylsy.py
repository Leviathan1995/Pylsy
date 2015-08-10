# -*- coding: utf-8 -*-
class PylsyTable:
    def __init__(self,attributes):
        self.Attributes=attributes
        self.Table=[]
        self.AttributesLength=[]
        self.Colsnum=len(self.Attributes)
        self.Linesnum=0
        for attribute in self.Attributes:
            col=dict()
            col[attribute]=""
            self.Table.append(col)
    def PrintDivide(self):
        for space in self.AttributesLength:
            print "+",
            for sign in range(space):
                print "-",
        print "+"
    def AddData(self,attribute,values):
        for col in self.Table:
            if col.has_key(attribute):
                dictvalues=[]
                for value in values:
                    if type(value)!=str:
                        dictvalues.append(str(value))
                    else:
                        dictvalues.append(value)
                col[attribute]=dictvalues
    def CreateTable(self):
        for col in self.Table:
            values=col.values()[0]
            if self.Linesnum<len(values):
                self.Linesnum=len(values)
            # find the length of longest word in current column
            Len=len(col.keys()[0])
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
            for col,length in zip(self.Table,self.AttributesLength):
                print "|",
                valuelength=length*2-1
                value=col.values()[0]
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
