from datetime import datetime, timedelta
from io import BytesIO
from unittest.mock import patch

import pandas as pd
import pytest

from tests.test_utils import sample_data
from tests.test_views import sample_greeting, sample_user_transactions, sample_top_transactions, sample_currency_rates, \
    sample_stock_prices


@pytest.fixture
def sample_data_excel():
    data = {
        'Дата операции': [
            '01.04.2024 12:00:00',
            '10.04.2024 13:30:00',
            '15.04.2024 09:20:00',
            '20.04.2024 18:00:00',
            '25.04.2024 14:15:00',
            '30.04.2024 08:50:00',
            '05.03.2024 11:10:00'
        ],
        'Сумма операции с округлением': [
            100.0,
            250.5,
            190.0,
            300.75,
            220.0,
            199.99,
            1000.0
        ]
    }
    df = pd.DataFrame(data)
    buffer = BytesIO()
    df.to_excel(buffer, index=False)
    buffer.seek(0)
    return buffer


@pytest.fixture
def sample_transactions():
    data = {
        'Категория': ['food', 'transport', 'food', 'utilities'],
        'Дата операции': [
            (datetime.now() - timedelta(days=10)).strftime('%d.%m.%Y'),
            (datetime.now() - timedelta(days=95)).strftime('%d.%m.%Y'),
            (datetime.now() - timedelta(days=30)).strftime('%d.%m.%Y'),
            (datetime.now() - timedelta(days=15)).strftime('%d.%m.%Y'),
        ],
        'Сумма': [100, 50, 200, 150]
    }
    return pd.DataFrame(data)

@pytest.fixture
def sample_datetime():
    return pd.Timestamp("2024-04-27 10:30:00")


@pytest.fixture
def mock_dependencies():
    with patch('src.views.day_time_now', return_value=sample_greeting) as mock_day_time_now,\
         patch('src.views.user_transactions', return_value=sample_user_transactions) as mock_user_transactions,\
         patch('src.views.max_five_transactions', return_value=sample_top_transactions) as mock_max_five_transactions,\
         patch('src.views.exchange_rate', return_value=sample_currency_rates) as mock_exchange_rate,\
         patch('src.views.get_price_stocks_snp500', return_value=sample_stock_prices) as mock_get_price_stocks_snp500:
        yield (mock_day_time_now, mock_user_transactions, mock_max_five_transactions, mock_exchange_rate, mock_get_price_stocks_snp500)

@pytest.fixture(autouse=True)
def mock_read_excel(monkeypatch):
    """Mock pd.read_excel to return sample_data instead of reading a file."""
    monkeypatch.setattr(pd, "read_excel", lambda *args, **kwargs: sample_data)