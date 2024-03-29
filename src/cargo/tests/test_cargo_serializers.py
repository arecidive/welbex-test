import pytest
from django.core.cache import cache

from location.models import Location
from truck.models import Truck

from .. import serializers
from ..models import Cargo


@pytest.mark.django_db
class TestCacheSerializer:
    """
    Класс представляет тесты для функции кэширования.
    """

    def test_get_trucks_cache(self, test_data: dict[str, Location | Truck | Cargo]) -> None:
        """
        Тест функции 'get_trucks_cache'. Проверяет корректность получения и кэширования грузовиков.
        """

        assert cache.get('trucks_cache') is None

        trucks = serializers.get_trucks_cache()

        assert cache.get('trucks_cache') is not None

        trucks_cached = serializers.get_trucks_cache()

        assert set(trucks_cached.values_list('id', flat=True)) == set(trucks.values_list('id', flat=True))


@pytest.mark.django_db
class TestCargoListSerializer:
    """
    Класс представляет тесты для 'CargoListSerializer'.
    """

    def test_cargo_list_serializer(self, test_data: dict[str, Location | Truck | Cargo]) -> None:
        """
        Тест проверяет корректность сериализации списка грузов с информацией о количестве ближайших грузовиков.
        """

        cargo = test_data['cargo_1']  # Груз находится рядом с 2-мя машинами
        serializer = serializers.CargoListSerializer(instance=cargo)

        assert 'nearest_trucks_count' in serializer.data
        assert serializer.data['nearest_trucks_count'] == 2

        cargo = test_data['cargo_2']  # Груз находится рядом с 2-мя машинами, но одной из них не подходит по весу
        serializer = serializers.CargoListSerializer(instance=cargo)

        assert serializer.data['nearest_trucks_count'] == 1

        cargo = test_data['cargo_3']  # Груз находится далеко от всех машин в базе данных
        serializer = serializers.CargoListSerializer(instance=cargo)

        assert serializer.data['nearest_trucks_count'] == 0


@pytest.mark.django_db
class TestCargoRetrieveSerializer:
    """
    Класс представляет тесты для 'CargoRetrieveSerializer'.
    """

    def test_cargo_list_serializer(self, test_data: dict[str, Location | Truck | Cargo]) -> None:
        """
        Тест проверяет корректность сериализации списка грузов с информацией о ближайших грузовиках.
        """

        cargo = test_data['cargo_1']  # Груз находится рядом с 2-мя машинами
        serializer = serializers.CargoRetrieveSerializer(instance=cargo)

        assert 'nearest_trucks' in serializer.data

        trucks_serializer = serializer.data['nearest_trucks']
        trucks = [
            test_data['truck_1'].number,
            test_data['truck_2'].number
        ]

        assert all(truck['truck_number'] in trucks for truck in trucks_serializer)
