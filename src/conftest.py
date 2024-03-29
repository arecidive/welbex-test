import pytest

from cargo.models import Cargo
from location.models import Location
from truck.models import Truck


@pytest.fixture
def location_1() -> Location:
    """
    Фикстура, создающая объект первой локации.

    :returns: объект первой локации.
    """

    return Location.objects.create(
        city='Test City 1',
        state='Test State 1',
        zip_code='99929',
        latitude=56.36089,
        longitude=-132.00635
    )


@pytest.fixture
def location_2() -> Location:
    """
    Фикстура, создающая объект второй локации.

    :returns: объект второй локации.
    """

    return Location.objects.create(
        city='Test City 2',
        state='Test State 2',
        zip_code='99927',
        latitude=56.33305,
        longitude=-133.60044
    )


@pytest.fixture
def location_3() -> Location:
    """
    Фикстура, создающая объект третьей локации.

    :returns: объект третьей локации.
    """

    return Location.objects.create(
        city='Test City 3',
        state='Test State 3',
        zip_code='99176',
        latitude=18.26319,
        longitude=-65.97938
    )


@pytest.fixture
def truck_1(location_1: Location) -> Truck:
    """
    Фикстура, создающая объект первой машины.

    :returns: объект первой машины.
    """

    return Truck.objects.create(
        number='9410P',
        current_location=location_1,
        capacity=250
    )


@pytest.fixture
def truck_2(location_1: Location) -> Truck:
    """
    Фикстура, создающая объект второй машины.

    :returns: объект второй машины.
    """

    return Truck.objects.create(
        number='4437R',
        current_location=location_1,
        capacity=712
    )


@pytest.fixture
def cargo_1(location_1: Location, location_2: Location) -> Cargo:
    """
    Фикстура, создающая объект первого груза.

    :returns: объект первого груза.
    """

    return Cargo.objects.create(
        pick_up_location=location_1,
        delivery_location=location_2,
        weight=127,
        description='Test Cargo 1'
    )


@pytest.fixture
def cargo_2(location_1: Location, location_2: Location) -> Cargo:
    """
    Фикстура, создающая объект второго груза.

    :returns: объект второго груза.
    """

    return Cargo.objects.create(
        pick_up_location=location_1,
        delivery_location=location_2,
        weight=617,
        description='Test Cargo 2'
    )


@pytest.fixture
def cargo_3(location_3: Location, location_1: Location) -> Cargo:
    """
    Фикстура, создающая объект третьего груза.

    :returns: объект третьего груза.
    """

    return Cargo.objects.create(
        pick_up_location=location_3,
        delivery_location=location_1,
        weight=50,
        description='Test Cargo 3'
    )


@pytest.fixture
def test_data(
        location_1: Location,
        location_2: Location,
        location_3: Location,
        truck_1: Truck,
        truck_2: Truck,
        cargo_1: Cargo,
        cargo_2: Cargo,
        cargo_3: Cargo
) -> dict[str, Location | Truck | Cargo]:
    """
    Фикстура, создающая словарь с тестовыми данными.

    :param location_1: фикстура объекта первой локации.
    :param location_2: фикстура объекта второй локации.
    :param location_3: фикстура объекта третьей локации.
    :param truck_1: фикстура объекта первой машины.
    :param truck_2: фикстура объекта второй машины.
    :param cargo_1: фикстура объекта первого груза.
    :param cargo_2: фикстура объекта второго груза.
    :param cargo_3: фикстура объекта третьего груза.

    :returns: словарь с тестовыми данными.
    """

    return {
        'location_1': location_1,
        'location_2': location_2,
        'location_3': location_3,
        'truck_1': truck_1,
        'truck_2': truck_2,
        'cargo_1': cargo_1,
        'cargo_2': cargo_2,
        'cargo_3': cargo_3
    }
