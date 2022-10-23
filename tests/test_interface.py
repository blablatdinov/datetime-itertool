import pytest

from datetime_itertool.datetime_iterator import DateTimeIteratorInterface


def test_interface():
    """Testing interface."""
    with pytest.raises(TypeError):
        iter(DateTimeIteratorInterface())  # type: ignore
    with pytest.raises(TypeError):
        next(iter(DateTimeIteratorInterface()))  # type: ignore
