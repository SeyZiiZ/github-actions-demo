import pytest
from calculator import average


def test_average_basic():
    assert average([1, 2, 3, 4, 5]) == 3.0


def test_average_single_element():
    assert average([10]) == 10.0


def test_average_floats():
    assert average([1.5, 2.5, 3.0]) == pytest.approx(2.333, rel=1e-2)


def test_average_negative():
    assert average([-1, -2, -3]) == -2.0


def test_average_empty_list():
    with pytest.raises(ValueError):
        average([])
