from __future__ import annotations

from typing import Any, Dict, Iterator, List

Transaction = Dict[str, Any]


def filter_by_currency(transactions: List[Transaction], currency_code: str) -> Iterator[Transaction]:
    """Filter transactions by currency code.

    Args:
        transactions: List of transactions (each transaction is a dict).
        currency_code: Currency code to filter by (for example, ``"USD"``).

    Yields:
        Transactions where ``transaction["operationAmount"]["currency"]["code"] == currency_code``.
        If a transaction does not have the required keys, it is simply skipped.
    """
    for transaction in transactions:
        currency = transaction.get("operationAmount", {}).get("currency", {})
        if currency.get("code") == currency_code:
            yield transaction


def transaction_descriptions(transactions: List[Transaction]) -> Iterator[str]:
    """Yield transaction descriptions one by one.

    Args:
        transactions: List of transactions (each transaction is a dict).

    Yields:
        The value of ``transaction["description"]`` for each transaction.
        If the key is missing, yields an empty string.
    """
    for transaction in transactions:
        yield str(transaction.get("description", ""))


def card_number_generator(start: int, end: int) -> Iterator[str]:
    """Generate bank card numbers in format ``XXXX XXXX XXXX XXXX``.

    The generator yields numbers in the inclusive range ``[start, end]``.
    Valid range is from ``1`` to ``9999 9999 9999 9999`` (i.e. ``9_999_999_999_999_999``).

    Args:
        start: Start of the range (inclusive).
        end: End of the range (inclusive).

    Yields:
        Card numbers as strings formatted like ``0000 0000 0000 0001``.

    Raises:
        ValueError: If the range is out of bounds or ``start > end``.
    """
    min_value = 1
    max_value = 9_999_999_999_999_999

    if start < min_value or end < min_value or start > max_value or end > max_value:
        raise ValueError("Card number range is out of bounds")
    if start > end:
        raise ValueError("Start must be less than or equal to end")

    for number in range(start, end + 1):
        digits = f"{number:016d}"
        yield f"{digits[0:4]} {digits[4:8]} {digits[8:12]} {digits[12:16]}"
