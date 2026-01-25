from typing import List, Dict, Any


def filter_by_state(
    data: List[Dict[str, Any]],
    state: str = "EXECUTED"
) -> List[Dict[str, Any]]:
    """
    Фильтрует список словарей по значению ключа state.
    По умолчанию возвращает операции со статусом EXECUTED.
    """
    return [item for item in data if item.get("state") == state]


def sort_by_date(
    data: List[Dict[str, Any]],
    reverse: bool = True
) -> List[Dict[str, Any]]:
    """
    Сортирует список словарей по дате.
    По умолчанию сортировка по убыванию (сначала новые).
    """
    return sorted(data, key=lambda x: x.get("date", ""), reverse=reverse)
