from __future__ import annotations

from typing import Literal, List, TypedDict, cast


class Operation(TypedDict, total=False):
    id: int
    state: str
    date: str


SortOrder = Literal["asc", "desc"]


def filter_by_state(data: List[Operation], state: str = "EXECUTED") -> List[Operation]:
    """
    Возвращает новый список операций, отфильтрованный по полю ``state``.
    """
    return [item for item in data if item.get("state") == state]


def sort_by_date(data: List[Operation], order: SortOrder = "desc") -> List[Operation]:
    """
    Возвращает новый список операций, отсортированный по полю ``date``.
    """
    reverse = order == "desc"

    def get_date(item: Operation) -> str:
        value = item.get("date", "")
        return cast(str, value)

    return sorted(data, key=get_date, reverse=reverse)
