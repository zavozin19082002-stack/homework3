import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "value, expected",
    [
        (1234123412341234, "1234 12** **** 1234"),
        (7000792289606361, "7000 79** **** 6361"),
    ],
)
def test_get_mask_card_number_ok(value, expected):
    assert get_mask_card_number(value) == expected


@pytest.mark.parametrize(
    "value, expected",
    [
        (12345678901234567890, "**7890"),
        (73654108430135874305, "**4305"),
    ],
)
def test_get_mask_account_ok(value, expected):
    assert get_mask_account(value) == expected


def test_get_mask_card_number_short_number_still_masks():
    # граничный случай: короткое число — функция всё равно маскирует строку
    assert isinstance(get_mask_card_number(123), str)


def test_get_mask_account_short_number_still_masks():
    assert get_mask_account(123) == "**123"
