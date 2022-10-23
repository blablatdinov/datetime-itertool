import datetime


class DateTimeIterator(object):
    """Iterating by time."""

    def __init__(
        self,
        start_datetime: datetime.datetime,
        finish_datetime: datetime.datetime,
    ):
        """Class constructor.

        :param start_datetime: datetime.datetime
        :param finish_datetime: datetime.datetime
        """
        self._start_datetime = start_datetime
        self._finish_datetime = finish_datetime
        self._shift = datetime.timedelta(days=0)

    def __iter__(self):
        """Iterator entrypoint.

        :return: DateTimeIterator
        """
        return self

    def __next__(self):
        """Iteration next value.

        :return: datetime.datetime
        :raises StopIteration: if iteration is ended
        """
        iteration_value = self._start_datetime + self._shift
        if iteration_value == self._finish_datetime:
            raise StopIteration
        self._shift += datetime.timedelta(days=1)
        return iteration_value
