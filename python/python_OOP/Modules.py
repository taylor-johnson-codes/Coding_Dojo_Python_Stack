# Modules are .py files that implement a set of functions
# use import keyword to use modules in other .py files
# all the .py files being utilized should be in the same directory/folder

# The first time a module is loaded into a running Python script, it is initialized by executing the code in the module once. 
# If another module in your code imports the same module again, it will not be loaded twice but once only - so local variables inside 
# the module act as a "singleton" - they are initialized only once.

# MODULE EXAMPLE:

# put this code in a file called arithmetic.py
def add(x, y):
    return x + y
def multiply(x, y):
    return x * y
def subtract(x, y):
    return x - y


# put this code in a file called calculations.py in the same directory/folder
import arithmetic
print(arithmetic.add(5, 8))
print(arithmetic.subtract(10, 5))
print(arithmetic.multiply(12, 6))


# PACKAGE EXAMPLE
# A package is a collection of modules in directories that give a package hierarchy.

# DIRECTORY:
# sample_project
#     |_____ python_file.py
#     |_____ my_modules  <-- This is the package name
#             |_____ __init__.py
#             |_____ test_module.py
#             |_____ another_module.py
#             |_____ third_module.py

# in .py file:
import my_modules.test_module
# or
from my_modules import test_module

# NOTES
# |_____ __init__.py  This file was required for all packages in Python 2.7; it would often be empty, but was required to indicate that the 
# files in the folder were part of the package. In Python 3.3+, we only need this file if we need to customize what modules are available to 
# anyone attempting to import the package. For example, if we didn't want another_module or third_module to be accessible for importing, 
# we could override the __all__ variable, like so:
# sample_project/my_modules/__init__.py
# __all__ = ["test_module"]