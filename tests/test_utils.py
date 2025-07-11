from src.utils import day_time_now, user_transactions, max_five_transactions

import datetime
import pytest
import pandas as pd


sample_data = pd.DataFrame({
    'Дата операции': ['01.09.2018 12:00:00', '15.09.2018 15:30:00', '20.09.2018 09:00:00', '10.09.2018 20:00:00', '25.09.2018 14:00:00', '29.08.2018 10:00:00'],
    'Номер карты': ['1234567890123456', '1234567890123456', '9876543210987654', '1234567890123456', '9876543210987654', '1234567890123456'],
    'Сумма операции с округлением': [1050, 2300, 1800, 100, 500, 700]
})

@pytest.mark.parametrize("mock_hour, expected_greeting", [
    (0, "Доброй ночи!"),
    (5, "Доброй ночи!"),
    (6, "Добрый день!"),
    (7, "Доброе утро!"),
    (11, "Доброе утро!"),
    (12, "Добрый день!"),
    (16, "Добрый день!"),
    (17, "Добрый вечер!"),
    (21, "Добрый вечер!"),
    (22, "Доброй ночи!"),
    (23, "Доброй ночи!"),
])
def test_day_time_now_greetings(monkeypatch, mock_hour, expected_greeting):
    class DummyDatetime(datetime.datetime):
        @classmethod
        def now(cls):
            return cls(2023, 1, 1, mock_hour, 0, 0)
    monkeypatch.setattr(datetime, 'datetime', DummyDatetime)
    assert day_time_now() == expected_greeting


def test_user_transactions(monkeypatch):
    test_date = pd.to_datetime('29-09-2018 00:00:00', dayfirst=True)
    result_df = user_transactions(test_date)
    assert set(result_df.columns) == {'Сумма операции с округлением', 'кэшбек'}
    assert all(isinstance(card, str) for card in result_df.index)
    for idx, row in result_df.iterrows():
        assert row['кэшбек'] == row['Сумма операции с округлением'] // 100


def test_max_five_transactions(monkeypatch):
    test_date = pd.to_datetime('29.09.2018', dayfirst=True)
    result_df = max_five_transactions(test_date)
    assert len(result_df) <= 5
    assert all(result_df['Сумма операции с округлением'].values[i] >= result_df['Сумма операции с округлением'].values[i + 1]
               for i in range(len(result_df) - 1))
    for dt_str in result_df['Дата операции']:
        dt = pd.to_datetime(dt_str, dayfirst=True)
        assert (dt <= test_date) and (dt.month == test_date.month)


