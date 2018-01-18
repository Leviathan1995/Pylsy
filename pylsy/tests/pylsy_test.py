# -*- coding: utf-8 -*-

from __future__ import absolute_import

import os
import unittest
from pylsy import pylsytable


TEST_DIR = os.path.dirname(__file__)


class PylsyTableTests(unittest.TestCase):

    def setUp(self):
        attributes = ["name", "age"]
        self.table = pylsytable(attributes)

    def tearDown(self):
        self.table = None

    def testCreateTable(self):
        name = ["a"]
        self.table.add_data("name", name)
        self.table.append_data("name", "b")
        age = [1, 2]
        self.table.add_data("age", age)

        with open(os.path.join(TEST_DIR, "correct.out"), "r") as correct_file:
            self.assertEqual(self.table.__str__(), correct_file.read())

    def testAddData(self):
        # Creating a table with data
        old_names = [
                "mercury",
                "venus",
                "earth"
        ]
        self.table.add_data("name", old_names)

        # This is necessary as it calls `create_table()`,
        # which calculates Lines_num property.
        # This is equivalent to calling `print table`
        self.table.__str__()

        # Overwriting existing table with new data
        new_names = [
                "mars",
                "jupiter"
        ]
        self.table.add_data("name", new_names)

        expected_output = "\n".join([
            "+ - - - - - - - + - - - +",
            "|     name      |  age  | ",
            "+ - - - - - - - + - - - +",
            "|     mars      |       |",
            "+ - - - - - - - + - - - +",
            "|    jupiter    |       |",
            "+ - - - - - - - + - - - +",
            ""
        ])

        output = self.table.__str__()

        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main()
