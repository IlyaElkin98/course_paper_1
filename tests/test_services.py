import json

import pytest
from src.services import simple_search

def test_simple_search_found_in_category_and_description():
    transactions = [
        {'Категория': 'Еда', 'Описание': 'Покупка в магазине'},
        {'Категория': 'Транспорт', 'Описание': 'Поездка на метро'},
        {'Категория': 'Еда', 'Описание': 'Ужин в ресторане'},
    ]
    # Search string in 'Категория'
    result = simple_search('Еда', transactions)
    expected = [
        {'Категория': 'Еда', 'Описание': 'Покупка в магазине'},
        {'Категория': 'Еда', 'Описание': 'Ужин в ресторане'},
    ]
    assert json.loads(result) == expected
    result = simple_search('метро', transactions)
    expected = [
        {'Категория': 'Транспорт', 'Описание': 'Поездка на метро'},
    ]
    assert json.loads(result) == expected

def test_simple_search_type_error():
    transactions = []
    with pytest.raises(TypeError) as excinfo:
        simple_search(123, transactions)
    assert "Неверный тип данных" in str(excinfo.value)

def test_simple_search_empty_search_string():
    transactions = [
        {'Категория': 'Связь', 'Описание': 'Оплата интернета'},
        {'Категория': 'Развлечения', 'Описание': 'Кинотеатр'},
    ]
    result = simple_search('', transactions)
    expected = transactions
    assert json.loads(result) == expected

@pytest.mark.parametrize(
    "search_str, transactions, expected_count",
    [
        ('а', [{'Категория': 'А', 'Описание': 'Б'}], 1),
        ('z', [{'Категория': 'x', 'Описание': 'y'}], 0),
        ('поездка', [{'Категория': 'Транспорт', 'Описание': 'Поездка на метро'}], 1),
    ]
)
def test_simple_search_parametrized(search_str, transactions, expected_count):
    result = simple_search(search_str, transactions)
    loaded = json.loads(result)
    assert len(loaded) == 0