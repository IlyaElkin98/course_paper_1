
from typing import Any

import pandas as pd

from src.reports import dir_transactions_excel, spending_by_category
from src.services import simple_search, dict_list
from src.views import website


def main() -> Any:
    """Функция для запуска всего проекта"""
    print("Функция для запуска всего проекта")


if __name__ == '__main__':
    print("\nГЛАВНАЯ\n")

    data_time = pd.Timestamp("29-09-2018 00:00:00")
    main_json = website(data_time)
    print(main_json)

    print("\nСЕРВИСЫ. ПРОСТОЙ ПОИСК\n")
    search_str = input('Введите строку поиска: ')
    simple_search(search_str, dict_list)

    print("\nОТЧЕТЫ\n")
    spending_by_category(pd.read_excel(dir_transactions_excel), 'Фастфуд', '11.11.2019')