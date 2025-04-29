
from pathlib import Path
from typing import Any, Dict, List

from logger import setup_logging

current_dir = Path(__file__).parent.parent.resolve()
file_path_log = current_dir/'../log', 'services.log'
logger = setup_logging('services', file_path_log)


def simple_search(search_str: str, transactions: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Функция, которая получает строку для поиска и список транзакций.
    Выводит список транзакций, в которых есть данная строка
    """

    if not isinstance(search_str, str):
        raise TypeError("Неверный тип данных")
    new_list_transactions = []
    for item in transactions:
        # print(item)
        if search_str in item['description']:
            new_list_transactions.append(item)

        elif search_str in item['state']:
            new_list_transactions.append(item)
        elif search_str in item['date']:
            new_list_transactions.append(item)
        elif search_str in item['from']:
            new_list_transactions.append(item)
        elif search_str in item['to']:
            new_list_transactions.append(item)
        elif search_str in str(item['id']):
            new_list_transactions.append(item)
        elif search_str in item['operationAmount']['amount']:
            new_list_transactions.append(item)
        elif search_str in item['operationAmount']['currency']['name']:
            new_list_transactions.append(item)
        elif search_str in item['operationAmount']['currency']['code']:
            new_list_transactions.append(item)

    result = new_list_transactions
    # result = json.dumps(new_list_transactions)
    logger.info("Вывод отфильтрованных по заданной пользователем строке транзакций")

    if search_str == "" or search_str == None or not transactions:
        return []
    # result_json = json.dumps(result, ensure_ascii=False)
    # print(result_json)
    if len(result) == 0:
        print("По вашему запросу ничего не найдено")
    else:
        print("Результат simple_search:", result)
    return result


transactions = (
    [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]
)


if __name__ == '__main__':
    search_str = input('Введите строку поиска: ')
    simple_search(search_str, transactions)
