from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(data: str) -> str:
    """
    Маскирует номер карты или счета в зависимости от типа.

    Принимает строку с названием и номером карты или счета.
    Возвращает строку с замаскированным номером.
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
    """
    date_part = date_str.split("T")[0]
    year, month, day = date_part.split("-")
    return f"{day}.{month}.{year}"
