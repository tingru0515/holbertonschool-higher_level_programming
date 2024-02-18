import sys, os, importlib

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

# Use __import__ for relative import
module_name = 'test_assets.custom_test'
module = importlib.import_module(module_name)

class ParentTest(module.CustomTest):
    path = 'python-almost_a_circle'
