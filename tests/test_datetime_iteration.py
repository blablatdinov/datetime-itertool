import datetime

import pytest

from datetime_itertool.datetime_iterator import DateTimeIterator


def test():
    """Testing DateTimeIterator class."""
    got = list(DateTimeIterator(
        datetime.datetime(2022, 2, 7),
        datetime.datetime(2022, 10, 23),
        step=datetime.timedelta(days=1),
    ))

    assert got[0] == datetime.datetime(2022, 2, 7)
    assert got[-1] == datetime.datetime(2022, 10, 22)
    assert len(got) == 258


@pytest.mark.parametrize(('start', 'end', 'step', 'expect_end', 'count'), [
    (
        datetime.datetime(2022, 2, 7),
        datetime.datetime(2022, 10, 23),
        datetime.timedelta(days=3),
        datetime.datetime(2022, 10, 20),
        86,
    ),
])
def test_with_step(start, end, step, expect_end, count):
    """Test with step."""
    got = list(DateTimeIterator(start, end, step))

    assert got[0] == start
    assert got[-1] == expect_end
    assert len(got) == count


def test_end_less_then_start():
    """Test end of iteration less than it start."""
    got = list(DateTimeIterator(
        datetime.datetime(2022, 10, 23),
        datetime.datetime(2022, 2, 7),
        step=datetime.timedelta(days=1),
    ))

    assert got == []  # noqa: WPS520 check test result is empty list
