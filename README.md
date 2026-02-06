# Homework 2

## Цель проекта
Проект предназначен для обработки списка банковских операций:
фильтрации по статусу, сортировки по дате и генераторов для обработки транзакций.

## Установка
1. Клонировать репозиторий:
   git clone https://github.com/zavozin19082002-stack/homework2.git
2. Перейти в папку проекта:
   cd homework2
3. Установить зависимости (если требуется):
   poetry install

## Использование

### filter_by_state
Функция фильтрует список операций по статусу `state`.

Пример:
```python
from src.processing.processing import filter_by_state

data = [
    {"id": 1, "state": "EXECUTED", "date": "2019-01-01T00:00:00"},
    {"id": 2, "state": "CANCELED", "date": "2019-01-02T00:00:00"},
]

print(filter_by_state(data))
print(filter_by_state(data, "CANCELED"))
```

### sort_by_state
Функция сортирует список операций по дате.
Пример:
```python
from src.processing.processing import sort_by_date

data = [
    {"id": 1, "state": "EXECUTED", "date": "2019-01-01T00:00:00"},
    {"id": 2, "state": "CANCELED", "date": "2018-01-01T00:00:00"},
]

print(sort_by_date(data))               # по убыванию (по умолчанию)
print(sort_by_date(data, order="asc"))  # по возрастанию
```

### Модуль generators
Модуль generators содержит генераторы для обработки транзакций:
filter_by_currency — фильтрует транзакции по коду валюты (например, "USD") и возвращает итератор.
transaction_descriptions — по очереди возвращает описания операций.
card_number_generator — генерирует номера карт в формате XXXX XXXX XXXX XXXX в заданном диапазоне.

### filter_by_currency
Пример:
```python
from src.generators import filter_by_currency

transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {"name": "USD", "code": "USD"}
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {
            "amount": "43318.34",
            "currency": {"name": "руб.", "code": "RUB"}
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160"
    }
]

usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(1):
    print(next(usd_transactions))
```

### transaction_descriptions
Пример: 
```python
from src.generators import transaction_descriptions

descriptions = transaction_descriptions(transactions)
for _ in range(2):
    print(next(descriptions))
```

### card_number_generator
Пример:
```python
from src.generators import card_number_generator

for card_number in card_number_generator(1, 5):
    print(card_number)
```