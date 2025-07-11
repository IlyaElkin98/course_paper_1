from unittest.mock import patch

import pandas as pd
import pytest

from src.views import website


import pytest
from unittest.mock import patch
import pandas as pd
from src.views import website

sample_greeting = "Добрый день"
sample_user_transactions = [
    {"card_last_4": "1234", "total_spent": 1000, "cashback": 10},
    {"card_last_4": "5678", "total_spent": 500, "cashback": 5}
]
sample_top_transactions = [
    {"transaction_id": 1, "amount": 300},
    {"transaction_id": 2, "amount": 250},
    {"transaction_id": 3, "amount": 200},
    {"transaction_id": 4, "amount": 150},
    {"transaction_id": 5, "amount": 100}
]
sample_currency_rates = {"USD": 73.5, "EUR": 87.1}
sample_stock_prices = {"AAPL": 145.6, "GOOG": 2730.7}

def test_website_returns_expected_keys_and_values(mock_dependencies):
    data_time = pd.Timestamp("2023-01-01 12:00:00")
    result = website(data_time)

    assert "greeting" in result
    assert "cards" in result
    assert "top_transactions" in result
    assert "currency_rates" in result
    assert "stock_prices" in result

    assert result["greeting"] == sample_greeting
    assert result["cards"] == sample_user_transactions
    assert result["top_transactions"] == sample_top_transactions
    assert result["currency_rates"] == sample_currency_rates
    assert result["stock_prices"] == sample_stock_prices

@pytest.mark.parametrize("input_datetime", [
    pd.Timestamp("2020-07-20 08:30:00"),
    pd.Timestamp("2021-12-31 23:59:59"),
    pd.Timestamp("2019-03-15 15:45:00")
])
def test_website_with_various_datetimes(input_datetime, mock_dependencies):
    result = website(input_datetime)
    assert isinstance(result, dict)
    assert result["greeting"] == sample_greeting
    assert isinstance(result["cards"], list)

def test_website_raises_type_error_on_invalid_input():
    with pytest.raises(TypeError):
        website("invalid-datetime-string")