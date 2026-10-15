import pytest

from stocklab import data, indicators


@pytest.fixture(scope="session")
def prices():
    return data.synthetic("TEST", years=4)


@pytest.fixture(scope="session")
def ind(prices):
    return indicators.add_all(prices)


@pytest.fixture(scope="session")
def panel():
    return {t: indicators.add_all(data.synthetic(t, years=4)) for t in ["AAA", "BBB", "CCC", "DDD"]}
