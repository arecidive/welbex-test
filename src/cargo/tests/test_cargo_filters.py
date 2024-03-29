import pytest
from rest_framework.test import APIRequestFactory

from location.models import Location
from truck.models import Truck

from ..filters import CargoFilterBackend
from ..models import Cargo
from ..views import CargoViewSet


@pytest.fixture
def api_request() -> APIRequestFactory:
    """
    Фикстура для создания запросов к API. Создает и возвращает экземпляр класса 'APIRequestFactory',
    который используется для отправки HTTP-запросов к API.

    :returns: экземпляр класса 'APIRequestFactory' для взаимодействия с API.
    """

    return APIRequestFactory()


@pytest.mark.django_db
class TestCargoFilterBackend:
    """
    Класс представляет тесты для 'CargoFilterBackend'.
    """

    def test_filter_queryset_by_weight(
            self,
            api_request: APIRequestFactory,
            test_data: dict[str, Location | Truck | Cargo]
    ) -> None:
        """
        Тест проверяет, что фильтр отбирает правильные объекты по запросу с указанным весом.
        """

        backend = CargoFilterBackend()
        cargo = test_data['cargo_1']

        request = api_request.get('cargo-list')
        request.query_params = {'weight': cargo.weight}

        queryset = backend.filter_queryset(request, Cargo.objects.all(), CargoViewSet)

        assert len(queryset) == 1
        assert cargo in queryset

    @pytest.mark.django_db
    def test_filter_queryset_by_truck_number(
            self,
            api_request: APIRequestFactory,
            test_data: dict[str, Location | Truck | Cargo]
    ) -> None:
        """
        Тест проверяет, что фильтр отбирает правильные объекты по запросу с номера машины,
        которая находится рядом с грузом.
        """

        backend = CargoFilterBackend()
        truck = test_data['truck_2']
        cargo_1, cargo_2 = test_data['cargo_1'], test_data['cargo_2']

        request = api_request.get('cargo-list')
        request.query_params = {'truck_number': truck.number}

        queryset = backend.filter_queryset(request, Cargo.objects.all(), CargoViewSet)

        assert len(queryset) == 2
        assert cargo_1 in queryset
        assert cargo_2 in queryset

    @pytest.mark.django_db
    def test_filter_queryset_by_truck_number_invalid_truck_invalid_weight(
            self,
            api_request: APIRequestFactory,
            test_data: dict[str, Location | Truck | Cargo]
    ) -> None:
        """
        Тест проверяет, что фильтр не отбирает объекты, с запросом, который содержит
        несуществующий вес в базе данных или несуществующий номер машины.
        """

        backend = CargoFilterBackend()

        request = api_request.get('cargo-list')
        request.query_params = {'truck_number': '0'}

        queryset = backend.filter_queryset(request, Cargo.objects.all(), CargoViewSet)

        assert len(queryset) == 0

        request = api_request.get('cargo-list')
        request.query_params = {'weight': '0'}

        queryset = backend.filter_queryset(request, Cargo.objects.all(), CargoViewSet)

        assert len(queryset) == 0
