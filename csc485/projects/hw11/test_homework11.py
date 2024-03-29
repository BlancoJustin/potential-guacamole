import pytest
import sci_name
from sci_name import get_formal_name
from sci_name import get_scientific_name

"""
Testables:
Testing a string in dictionary
Testing a string not in dictionary
Testing floats and ints (not in dictionary)
Testing list of fruits in dictionary
Testing empty string
"""

"""
Testing for initial method
"""
def test_get_formal_name_apple():
    formal_name = get_formal_name('apple')
    assert formal_name == 'Malus domestica'

def test_get_formal_name_vegetable():
    formal_name = get_formal_name('carrot')
    assert formal_name is None

def test_get_formal_name_int():
    formal_name = get_formal_name(12)
    assert formal_name is None

def test_get_formal_name_float():
    formal_name = get_formal_name(1.2)
    assert formal_name is None

def test_get_formal_name_empty_string():
    formal_name = get_formal_name('')
    assert formal_name is None

def test_get_formal_name_list_of_fruits():
    fruits = ['mango', 'blueberry', 'cherry']
    formal_names = get_formal_name(fruits)
    assert formal_names == ['Mangifera indica', 'Vaccinium corymbosum', 'Prunus avium']

"""
Testing for new method
"""
def test_get_scientific_name_apple():
    scientific_name = get_scientific_name('apple')
    assert scientific_name == 'Malus domestica'

def test_get_scientific_name_vegetable():
    scientific_name = get_scientific_name('carrot')
    assert scientific_name == 'Unknown'

def test_get_scientific_name_int():
    scientific_name = get_scientific_name('12')
    assert scientific_name == 'Unknown'

def test_get_scientific_name_float():
    scientific_name = get_scientific_name(1.5)
    assert scientific_name == 'Unknown'

def test_get_scientific_name_empty_string():
    scientific_name = get_scientific_name('')
    assert scientific_name == 'Unknown'

def test_get_scientific_name_list_of_fruits():
    fruits = ['mango', 'blueberry', 'cherry']
    scientific_names = get_formal_name(fruits)
    assert scientific_names == ['Mangifera indica', 'Vaccinium corymbosum', 'Prunus avium']

