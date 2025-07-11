import pytest
from src.reports import spending_by_category


def test_spending_by_category_invalid_date_format(sample_transactions):
    with pytest.raises(ValueError):
        spending_by_category(sample_transactions, category='Еда', date='invalid-date')


