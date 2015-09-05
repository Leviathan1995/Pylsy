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

if __name__ == '__main__':
    unittest.main()
