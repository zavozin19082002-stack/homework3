import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "value, expected_piece",
    [
        ("Maestro 1234123412341234", "12** **** 1234"),
        ("Счет 73654108430135874305", "**4305"),
    ],
)
def test_mask_account_card_ok(value, expected_piece):
    result = mask_account_card(value)
    assert expected_piece in result


@pytest.mark.parametrize(
    "value",
    [
        "",                 # пусто
        "Счет",             # нет номера
        "Maestro",          # нет номера
        "что-то непонятное" # нет числа
    ],
)
def test_mask_account_card_bad_input(value):
    with pytest.raises(Exception):
        mask_account_card(value)


def test_get_date_ok():
    assert get_date("2018-10-14T08:21:33.419441") == "14.10.2018"


import pytest

@pytest.mark.parametrize("value", ["", "not-a-date"])
def test_get_date_bad_input(value):
    with pytest.raises(ValueError):
        get_date(value)


