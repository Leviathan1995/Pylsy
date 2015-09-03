# -*- coding: utf-8 -*-

from __future__ import absolute_import
import unittest
import sys
sys.path.append('..')
from pylsy import pylsytable


class PylsyTableTests(unittest.TestCase):

    def setUp(self):
        attributes = ["name", "age"]
        self.table = pylsytable(attributes)

    def tearDown(self):
        self.table = None

    def testCreateTable(self):
        name = ["a", "b"]
        self.table.add_data("name", name)
        age = [1, 2]
        self.table.add_data("age", age)
        correct_file = open('correct.out', 'r')
        correctPrint = correct_file.read()
        try:
            import io
            from contextlib import redirect_stdout
            with io.StringIO() as buf, redirect_stdout(buf):
                print('redirected')
                output = buf.getvalue()
                self.assertEqual(output, correctPrint)
        except ImportError:
            import sys
            f_handler = open('test.out', 'w')
            sys.stdout = f_handler
            print(self.table)
            f_handler.close()
            f_handler = open('test.out', 'r')
            self.assertEqual(f_handler.read(), correctPrint)

if __name__ == '__main__':
    unittest.main()
