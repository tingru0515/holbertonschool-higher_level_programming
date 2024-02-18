import unittest
import os
import sys
import subprocess

BaseModule = __import__('models.base', fromlist=['Base'])
Base = BaseModule.Base
sys.path.append("../..")


class BaseTest(unittest.TestCase):
    """
    Test case for the Base class.
    """

    def test_pycodestyle(self):
        """
        Test pycodestyle.
        """
        command = ["pycodestyle", 'models/base.py']
        result = subprocess.run(
            command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        self.assertEqual(result.returncode, 0,
                         f"pycodestyle check failed:\n{result.stdout}")

    def test_init_without_id(self):
        """
        Test the initialization without providing an ID.
        """
        instance = Base()
        actual_value = instance.id
        expected_value = 1
        self.assertEqual(actual_value, expected_value)

    def test_init_id(self):
        """
        Test the initialization with a specified ID.
        """
        instance = Base(90)
        actual_value = instance.id
        expected_value = 90
        self.assertEqual(actual_value, expected_value)

    def test_to_json_string_with_list_dictionaries(self):
        """
        Test the to_json_string method with a list of dictionaries.
        """
        list_dictionaries = [{'x': 1, 'y': 3}]
        actual_value = Base.to_json_string(list_dictionaries)
        expected_value = '[{"x": 1, "y": 3}]'
        self.assertEqual(actual_value, expected_value)

    def test_to_json_string_with_empty_list(self):
        """
        Test the to_json_string method with an empty list.
        """
        list_dictionaries = []
        actual_value = Base.to_json_string(list_dictionaries)
        expected_value = '[]'
        self.assertEqual(actual_value, expected_value)

    def test_to_json_string_with_none(self):
        """
        Test the to_json_string method with None.
        """
        list_dictionaries = None
        actual_value = Base.to_json_string(list_dictionaries)
        expected_value = '[]'
        self.assertEqual(actual_value, expected_value)

    def test_from_json_string(self):
        """
        Test the from_json_string method.
        """
        json_string = '[{"x": 1, "y": 3}]'
        actual_value = Base.from_json_string(json_string)
        expected_value = [{'x': 1, 'y': 3}]
        self.assertEqual(actual_value, expected_value)

    def test_from_json_string_with_empty_string(self):
        """
        Test the from_json_string method with an empty string.
        """
        json_string = ''
        actual_value = Base.from_json_string(json_string)
        expected_value = []
        self.assertEqual(actual_value, expected_value)

    def test_from_json_string_with_none(self):
        """
        Test the from_json_string method with None.
        """
        json_string = None
        actual_value = Base.from_json_string(json_string)
        expected_value = []
        self.assertEqual(actual_value, expected_value)

    def test_from_json_string_with_obj_string(self):
        """
        Test the from_json_string method with an object string.
        """
        json_string = '{"x": 1, "y": 3}'
        actual_value = Base.from_json_string(json_string)
        expected_value = {"x": 1, "y": 3}
        self.assertEqual(actual_value, expected_value)

    # def test_save_to_file(self):
    #     list_objs = [{'x': 1, 'y': 3}]
    #     Base.save_to_file(list_objs)
    #     filename = "Base.json"
    #     self.assertTrue(os.path.exists(filename),
    #                     f"File '{filename}' does not exist")

    def test_save_to_file_from_base(self):
        """
        Test the save_to_file method from the Base class.
        """
        list_objs = [{'x': 1, 'y': 3}]
        with self.assertRaises(AttributeError):
            Base.save_to_file(list_objs)

    def test_create_from_base(self):
        """
        Test the create method from the Base class.
        """
        with self.assertRaises(TypeError):
            Base.create(1)

    def test_load_from_file_without_file(self):
        """
        Test the load_from_file method without a file.
        """
        filename = 'Base.json'
        if os.path.exists(filename):
            os.remove(filename)
        actual_value = Base.load_from_file()
        expected_value = []
        self.assertEqual(actual_value, expected_value)
