def get_mask_card_number(card_number: int) -> str:
    """
    Маскирует номер банковской карты.

    Формат маски: XXXX XX** **** XXXX.
    Отображаются первые 6 и последние 4 цифры номера карты.
    """
    card_str = str(card_number)
    first_six = card_str[:6]
    last_four = card_str[-4:]
    return f"{first_six[:4]} {first_six[4:6]}** **** {last_four}"


def get_mask_account(account_number: int) -> str:
    """
    Маскирует номер банковского счета.

    Формат маски: **XXXX.
    Отображаются только последние 4 цифры номера счета.
    """
    account_str = str(account_number)
    return f"**{account_str[-4:]}"
