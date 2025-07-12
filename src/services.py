import json
from pathlib import Path
from typing import Any, Dict, List


import pandas as pd

from logger import setup_logging

current_dir = Path(__file__).parent.parent.resolve()
file_path_log = current_dir/'../log', 'services.log'
logger = setup_logging('services', file_path_log)
dir_transactions_excel = current_dir/'data'/'operations.xlsx'
df = pd.read_excel(dir_transactions_excel)
dict_list = df.to_dict(orient='records')

def simple_search(search_str: str, dict_list: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Функция, которая получает строку для поиска и список транзакций.
    Выводит список транзакций, в которых есть данная строка
    """

    if not isinstance(search_str, str):
        raise TypeError("Неверный тип данных")
    new_list_transactions = []

    for item in dict_list:
        # print(item)
        if search_str in str(item['Категория']):
            new_list_transactions.append(item)
        elif search_str in item['Описание']:
            new_list_transactions.append(item)

    # print(new_list_transactions)


    result = json.dumps(new_list_transactions, ensure_ascii=False)
    logger.info("Вывод отфильтрованных по заданной пользователем строке транзакций")

    if len(result) == 0:
        print("По вашему запросу ничего не найдено")
    else:
        print("Результат поиска:", result)
    return result

if __name__ == '__main__':
    search_str = input('Введите строку поиска: ')
    simple_search(search_str, dict_list)



