import pytest

from processing.processing import filter_by_state, sort_by_date


def test_filter_by_state_default_executed(operations):
    result = filter_by_state(operations)
    assert len(result) == 2
    assert all(item["state"] == "EXECUTED" for item in result)


@pytest.mark.parametrize(
    "state, expected_count",
    [
        ("EXECUTED", 2),
        ("CANCELED", 2),
        ("UNKNOWN", 0),
    ],
)
def test_filter_by_state_parametrized(operations, state, expected_count):
    result = filter_by_state(operations, state=state)
    assert len(result) == expected_count
    if expected_count:
        assert all(item["state"] == state for item in result)


def test_sort_by_date_desc_default(operations):
    result = sort_by_date(operations)
    dates = [item.get("date", "") for item in result]
    assert dates == sorted(dates, reverse=True)


def test_sort_by_date_asc(operations):
    result = sort_by_date(operations, order="asc")
    dates = [item.get("date", "") for item in result]
    assert dates == sorted(dates)


def test_sort_by_date_same_dates_keeps_all(operations_same_dates):
    result = sort_by_date(operations_same_dates)
    assert len(result) == len(operations_same_dates)


def test_sort_by_date_with_missing_date_key():
    data = [{"id": 1, "state": "EXECUTED"}, {"id": 2, "state": "EXECUTED", "date": "2019-01-01T00:00:00"}]
    result = sort_by_date(data)
    assert len(result) == 2
