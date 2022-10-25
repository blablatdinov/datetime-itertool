import datetime
from collections.abc import Generator
from typing import Dict, Literal, Union

from datetime_itertool.exceptions import InvalidStepParamError

TIMEDELTA_AVAILABLE_PARAMS = (
    'days',
    'seconds',
    'microseconds',
    'milliseconds',
    'minutes',
    'hours',
    'weeks',
)
CUSTOM_SUPPORTABLE_SHIFT = (
    'years',
    'months',
)
INPUT_TYPE = Union[
    Dict[Literal[TIMEDELTA_AVAILABLE_PARAMS], float],
    Dict[Literal[CUSTOM_SUPPORTABLE_SHIFT], int],
]


class Step(Generator):
    """Step for iterator."""

    _timedelta_available_params = TIMEDELTA_AVAILABLE_PARAMS
    _custom_supportable_shift = CUSTOM_SUPPORTABLE_SHIFT
    _available_params = _timedelta_available_params + _custom_supportable_shift
    _month_in_year = 12
    _days_on_year = 365

    def __init__(
        self,
        **kwargs: INPUT_TYPE,
    ) -> None:
        """Class constructor."""
        self._kwargs = kwargs

    def __next__(self) -> datetime.timedelta:
        """Return next value.

        :return: datetime.timedelta
        :raises InvalidStepParamError: if parameter not valid
        """
        time_shift, count = list(self._kwargs.items())[0]
        if time_shift in self._timedelta_available_params:
            return datetime.timedelta(**self._kwargs)
        elif time_shift == 'years':
            return datetime.timedelta(days=self._days_on_year * count)
        elif time_shift == 'months':
            return self._moths_case(count)
        else:
            raise InvalidStepParamError(
                'Invalid param "{0}". Select between {1}'.format(
                    time_shift,
                    self._available_params,
                ),
            )

    def send(self):
        """collections.abc.Generator method override."""
        raise NotImplementedError

    def throw(self):
        """collections.abc.Generator method override."""
        raise NotImplementedError

    def _moths_case(self, month_count: int) -> datetime.timedelta:
        now_date = datetime.datetime.now()
        print(f'{now_date=}')
        print(f'{month_count=}')
        months_nums = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
        month = months_nums[((now_date.month + month_count) % 12) - 1]
        target_year = now_date.year
        if month_count + now_date.month >= 12:
            print(f'{(month_count + now_date.month)=}')
            print(f'{(month_count + now_date.month) // 12=}')
            # target_year = now_date.year + ((month_count + now_date.month) // 12)
            target_year = now_date.year + (month_count // 12) + 1
            print(f'{target_year=}')
            #target_year = now_date.year + 1
        target_date = now_date.replace(
            year=target_year,
            month=month,
        )
        print(f'{target_date=}')
        return target_date - now_date
