from parent_test import ParentTest
import unittest
import os
import sys

sys.path.append(os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")))

from models import rectangle

filename = "models/rectangle.py"


class TestTask0(ParentTest):

    def test_common_test(self):
        """ Testing a common stuff. check abstract_test/commontest"""

        self.common_test(filename)

    def test_module_doc(self):
        """ Testing module doc exists. """

        self.assertTrue(rectangle.__doc__)

    def test_class_doc(self):

        self.assertTrue(rectangle.Rectangle.__doc__)


if __name__ == "__main__":
    unittest.main()
