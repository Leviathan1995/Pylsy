# -*- coding: utf-8 -*-

from __future__ import print_function


class pylsytable(object):

    def __init__(self, attributes):
        self.StrTable = ""
        self.Attributes = attributes
        self.Table = []
        self.AttributesLength = []
        self.Cols_num = len(self.Attributes)
        self.Lines_num = 0
        for attribute in self.Attributes:
            col = dict()
            col[attribute] = ""
            self.Table.append(col)

    def print_divide(self):
        for space in self.AttributesLength:
            self.StrTable += "+ "
            for sign in range(space):
                self.StrTable += "- "
        self.StrTable += "+"+"\n"

    def add_data(self, attribute, values):
        for col in self.Table:
            if attribute in col:
                dict_values = [str(value) for value in values]
                col[attribute] = dict_values

    def create_table(self):
        self.StrTable = ""
        self.AttributesLength = []
        for col in self.Table:
            values = list(col.values())[0]
            if self.Lines_num < len(values):
                self.Lines_num = len(values)
            # find the length of longest word in current column

            key_length = len(list(col.keys())[0])
            for value in values:
                length = len(value)
                if length > key_length:
                    key_length = length
            self.AttributesLength.append(key_length)
        self.print_head()
        self.print_value()

    def print_head(self):
        self.print_divide()
        self.StrTable += "| "
        for spaces, attr in zip(self.AttributesLength, self.Attributes):
            space_num = spaces * 2 - 1
            start = (space_num - len(attr)) // 2
            for space in range(start):
                self.StrTable += " "
            self.StrTable += attr+' '
            end = space_num - start - len(attr)
            for space in range(end):
                self.StrTable += " "
            self.StrTable += "| "
        self.StrTable += ""+'\n'
        self.print_divide()

    def print_value(self):
        for line in range(self.Lines_num):
            for col, length in zip(self.Table, self.AttributesLength):
                self.StrTable += "| "
                value_length = length * 2 - 1
                value = list(col.values())[0]
                if len(value) != 0:
                    if line < len(value):
                        start = (value_length - len(value[line])) // 2
                        for space in range(start):
                            self.StrTable += " "
                        self.StrTable += value[line]+' '
                        end = value_length - start - len(value[line])
                        for space in range(end):
                            self.StrTable += " "
                    else:
                        start = 0
                        end = value_length - start + 1
                        for space in range(end):
                            self.StrTable += " "
                else:
                    start = 0
                    end = value_length - start + 1
                    for space in range(end):
                        self.StrTable += " "
            self.StrTable += "|"+'\n'
            self.print_divide()

    def __str__(self):
        self.create_table()
        return self.StrTable
