import pytest

from astropy.constants import Constant
from astropy.table import Table

from sunpy.sun import constants as con


def test_find_all():
    assert isinstance(con.find(), list)
    assert len(con.find()) == 34


def test_print_all():
    table = con.print_all()
    assert isinstance(table, Table)
    assert len(table) == 34


@pytest.mark.parametrize('this_constant', [value for key, value in con.constants.items()])
def test_all_constants_are_constants(this_constant):
    """
    Test that each member of the constants dict is an astropy Constant.
    """
    assert isinstance(this_constant, Constant)


@pytest.mark.parametrize('this_key', [key for key, value in con.constants.items()])
def test_get_function(this_key):
    """
    Test that the get function works for all the keys.
    """
    assert isinstance(con.get(this_key), Constant)


@pytest.mark.parametrize('this_key', [key for key, value in con.constants.items()])
def test_find_function(this_key):
    """
    Test that the find function works for all the keys.
    """
    assert len(con.find(this_key)) >= 1


@pytest.mark.parametrize('this_key', [key for key, value in con.constants.items()])
def test_find_function2(this_key):
    """
    Test that the find function works for all the keys.
    """
    assert len(con.find(this_key)) >= 1


@pytest.mark.parametrize("test_input", ['boo', 'crab', 'foo'])
def test_find_function3(test_input):
    """
    Test that the find function fails as expected.
    """
    assert len(con.find(test_input)) == 0
