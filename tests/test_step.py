import datetime

import pytest

from datetime_itertool.exceptions import InvalidStepParamError
from datetime_itertool.step import Step


@pytest.mark.parametrize(('step_input', 'on_date', 'expected'), [
    ({'days': 1}, '2022-10-24', datetime.timedelta(days=1)),
    ({'seconds': 5}, '2022-10-24', datetime.timedelta(seconds=5)),
    ({'weeks': 5}, '2022-10-24', datetime.timedelta(days=35)),
    ({'years': 8}, '2022-10-24', datetime.timedelta(days=2920)),
    ({'months': 1}, '2022-10-24', datetime.timedelta(days=31)),
    ({'months': 5}, '2022-10-24', datetime.timedelta(days=151)),
    ({'months': 50}, '2022-10-24', datetime.timedelta(days=1522)),
    ({'months': 1}, '2022-11-24', datetime.timedelta(days=30)),
    ({'months': 1}, '2022-12-24', datetime.timedelta(days=31)),
    ({'months': 30}, '2030-01-01', datetime.timedelta(days=912)),
])
def test(freezer, step_input, on_date, expected):
    """Test Step class."""
    freezer.move_to(on_date)
    step = Step(**step_input)

    assert next(step) == expected


def test_invalid_param():
    """Test Step with invalid param."""
    with pytest.raises(InvalidStepParamError):
        next(Step(foo=1))


def test_invalid_param_err_text():
    """Test Step with invalid param error text."""
    try:
        next(Step(foo=1))
    except InvalidStepParamError as err:
        assert 'Invalid param "foo". Select between' in str(err)


def test_not_implemented_methods():
    """Test Step not implemented methods."""
    with pytest.raises(NotImplementedError):
        Step(days=1).send()
    with pytest.raises(NotImplementedError):
        Step(days=1).throw()
