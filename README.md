# Homework 2

## Цель проекта
Проект предназначен для обработки списка банковских операций:
фильтрации по статусу и сортировки по дате.

## Установка
1. Клонировать репозиторий:
   git clone https://github.com/zavozin19082002-stack/homework2.git
2. Перейти в папку проекта:
   cd homework2
3. Установить зависимости (если требуется):
   poetry install

## Использование

### filter_by_state
Функция фильтрует список операций по статусу state.

Пример:
```python
from src.processing.processing import filter_by_state

data = [
    {"id": 1, "state": "EXECUTED", "date": "2019-01-01T00:00:00"},
    {"id": 2, "state": "CANCELED", "date": "2019-01-02T00:00:00"},
]

print(filter_by_state(data))
print(filter_by_state(data, "CANCELED"))
