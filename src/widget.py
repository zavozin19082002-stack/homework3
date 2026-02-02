from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(data: str) -> str:
    """
    Маскирует номер карты или счета в зависимости от типа.

    Принимает строку с названием и номером карты или счета.
    Возвращает строку с номером с маской.
    """
    parts = data.split()
    number = parts[-1]
    name = " ".join(parts[:-1])

    if name == "Счет":
        masked_number = get_mask_account(int(number))
    else:
        masked_number = get_mask_card_number(int(number))

    return f"{name} {masked_number}"

def get_date(date_str: str) -> str:
    """
    Преобразует дату из формата ISO в формат ДД.ММ.ГГГГ.
    Ожидаемый формат: YYYY-MM-DDTHH:MM:SS...
    """
    if not date_str or "T" not in date_str:
        raise ValueError("Invalid date format")

    date_part = date_str.split("T")[0]  # YYYY-MM-DD
    parts = date_part.split("-")
    if len(parts) != 3:
        raise ValueError("Invalid date format")

    year, month, day = parts
    if len(year) != 4 or len(month) != 2 or len(day) != 2:
        raise ValueError("Invalid date format")

    return f"{day}.{month}.{year}"

