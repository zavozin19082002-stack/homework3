import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "src"
sys.path.insert(0, str(SRC_PATH))


import pytest


@pytest.fixture
def operations():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 2, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 3, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 4, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def operations_same_dates():
    return [
        {"id": 10, "state": "EXECUTED", "date": "2019-01-01T00:00:00.000000"},
        {"id": 11, "state": "CANCELED", "date": "2019-01-01T00:00:00.000000"},
        {"id": 12, "state": "EXECUTED", "date": "2018-01-01T00:00:00.000000"},
    ]
