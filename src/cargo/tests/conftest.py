import pytest
from django.core.cache import cache


@pytest.fixture(autouse=True)
def clear_cache() -> None:
    """
    Фикстура для очистки кэша перед каждым тестом.
    """

    yield
    cache.clear()
