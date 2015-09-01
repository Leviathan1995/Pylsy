# -*- coding: utf-8 -*-
from __future__ import print_function

class PylsyTable(object):
    def __init__(self, attributes):
        self.Attributes = attributes
        self.Table = []
        self.AttributesLength = []
        self.cols_num = len(self.Attributes)
        self.lines_num = 0
        for attribute in self.Attributes:
            col = dict()
            col[attribute] = ""
            self.Table.append(col)

    def print_divide(self):
        for space in self.AttributesLength:
            print("+ ", end='')
            for sign in range(space):
                print("- ", end='')
        print("+")

    def add_data(self, attribute, values):
        for col in self.Table:
            if attribute in col:
                dict_values = [str(value) for value in values]
                col[attribute] = dict_values

    def create_table(self):
        for col in self.Table:
            values = list(col.values())[0]
            if self.lines_num < len(values):
                self.lines_num = len(values)
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
        print("| ", end='')
        for spaces, attr in zip(self.AttributesLength, self.Attributes):
            space_num = spaces * 2 - 1
            start = (space_num - len(attr)) // 2
            for space in range(start):
                print(" ", end='')
            print(attr + ' ', end='')
            end = space_num - start - len(attr)
            for space in range(end):
                print(" ", end='')
            print("| ", end='')
        print("")
        self.print_divide()

    def print_value(self):
        for line in range(self.lines_num):
            for col, length in zip(self.Table, self.AttributesLength):
                print("| ", end='')
                value_length = length * 2 - 1
                value = list(col.values())[0]
                if len(value) != 0:
                    start = (value_length - len(value[line])) // 2
                    for space in range(start):
                        print(" ", end='')
                    print(value[line] + ' ', end='')
                    end = value_length - start - len(value[line])
                    for space in range(end):
                        print(" ", end='')
                else:
                    start = 0
                    end = value_length - start + 1
                    for space in range(end):
                        print(" ", end='')
            print("|")
            self.print_divide()
