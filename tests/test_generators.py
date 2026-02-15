import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency_returns_only_requested_currency(transactions):
    usd_iter = filter_by_currency(transactions, "USD")
    first = next(usd_iter)
    assert first["operationAmount"]["currency"]["code"] == "USD"


def test_filter_by_currency_no_matches(transactions):
    eur_iter = filter_by_currency(transactions, "EUR")
    assert list(eur_iter) == []


def test_filter_by_currency_empty_list():
    it = filter_by_currency([], "USD")
    assert list(it) == []


def test_transaction_descriptions_returns_in_order(transactions):
    desc_iter = transaction_descriptions(transactions)
    assert next(desc_iter) == "Перевод организации"
    assert next(desc_iter) == "Перевод со счета на счет"


def test_transaction_descriptions_empty_list():
    desc_iter = transaction_descriptions([])
    assert list(desc_iter) == []


@pytest.mark.parametrize(
    "start,end,expected",
    [
        (1, 1, ["0000 0000 0000 0001"]),
        (
            1,
            5,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004",
                "0000 0000 0000 0005",
            ],
        ),
    ],
)
def test_card_number_generator_range(start, end, expected):
    assert list(card_number_generator(start, end)) == expected


def test_card_number_generator_formatting():
    value = next(card_number_generator(42, 42))
    assert value == "0000 0000 0000 0042"
    assert len(value) == 19
    assert value.count(" ") == 3


@pytest.mark.parametrize(
    "start,end",
    [
        (0, 1),
        (1, 0),
        (2, 1),
        (1, 10_000_000_000_000_000),
    ],
)
def test_card_number_generator_invalid_bounds(start, end):
    with pytest.raises(ValueError):
        list(card_number_generator(start, end))
