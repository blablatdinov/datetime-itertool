import datetime

from datetime_itertool.datetime_iterator import DateTimeIterator


def test():
    """Testing DateTimeIterator class."""
    got = list(DateTimeIterator(
        datetime.datetime(2022, 2, 7),
        datetime.datetime(2022, 10, 23),
    ))

    assert got[0] == datetime.datetime(2022, 2, 7)
    assert got[-1] == datetime.datetime(2022, 10, 22)
