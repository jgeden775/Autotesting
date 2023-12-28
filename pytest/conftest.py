import pytest

# Переменные браузеров
@pytest.fixture()
def firefox():
    return 'firefox'

@pytest.fixture()
def chrome():
    return 'chrome'

@pytest.fixture()
def edge():
    return 'edge'