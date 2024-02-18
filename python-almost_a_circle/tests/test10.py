from parent_test import ParentTest
import unittest
import os
import sys

sys.path.append(os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")))

from models import square


filename = "models/square.py"


class TestTask10(ParentTest):

    def test_common_test(self):
        """ Testing a common stuff. check abstract_test/commontest"""

        self.common_test(filename)

    def test_module_doc(self):
        """ Testing module doc exists. """

        self.assertTrue(square.__doc__)

    def test_class_doc(self):

        self.assertTrue(square.Square.__doc__)


if __name__ == "__main__":
    unittest.main()
