# -*- coding: utf-8 -*-
class Ptable:
    def __init__(self,type,attributenames):
        self.Type=type
        self.Attributenames=attributenames
        self.Table=[]
        for attr in attributenames:
            levia=dict()
            levia[attr]=""
            self.Table.append(levia)
    def AddData(self,attrname,content):
            for table in self.Table:
                if table.has_key(attrname):
                    table[attrname]=content

    def CreateTable(self):
        for attr in self.Attributenames:
            if self.Type=="Row":
                AttributesLength=[]
                for attrcontent in self.Table:
                    contents=attrcontent.values()
                    Len=0
                    for content in contents:
                        for item in content:
                            length=len(item)
                            if length>Len:
                                Len=length
                    AttributesLength.append(Len)
                    for attr in self.Attributenames:
                        for sign in range(len(AttributesLength)):
                            signlen=AttributesLength[sign]
                            print "+",
                            for spacenum in range(signlen):
                                print "-",







def main():
    table=Ptable("Row",["姓名","年龄"])
    table.AddData("姓名",["孙海清","刘斯阳"])
    table.CreateTable()


if __name__=='__main__':
    main()