from django.conf import settings
from django.core.cache import cache
from django.db.models import QuerySet
from geopy.distance import geodesic
from rest_framework import serializers

from location.models import Location
from truck.models import Truck

from .models import Cargo


def get_trucks_cache() -> QuerySet:
    """
    Функция получает кэш грузовиков из хранилища кэша. Если кэш грузовиков не существует, извлекает
    грузовики из базы данных, выбирая только номера грузовиков и текущее местоположение, и сохраняет их
    в кэше на 60 секунд.

    :returns: кэш грузовиков, содержащий информацию о номерах грузовиков и их текущем местоположении.
    """

    trucks_cache = cache.get(settings.TRUCKS_CACHE_NAME)
    if trucks_cache is None:
        trucks_cache = Truck.objects.only('number', 'current_location').select_related('current_location')
        cache.set(settings.TRUCKS_CACHE_NAME, trucks_cache, 60)
    return trucks_cache


class CargoBaseSerializer(serializers.ModelSerializer):
    """
    Класс представляет сериализатор для базовых полей груза.
    """

    pick_up_location_zip = serializers.SlugRelatedField(
        slug_field='zip_code',
        read_only=True,
        source='pick_up_location'
    )

    delivery_location_zip = serializers.SlugRelatedField(
        slug_field='zip_code',
        read_only=True,
        source='delivery_location'
    )


class CargoUpdateSerializer(CargoBaseSerializer):
    """
    Класс представляет сериализатор для обновления информации о грузе.
    """

    class Meta:
        """
        Класс для определения метаданных класса сериализатора.
        """

        model = Cargo
        fields = ('pick_up_location_zip', 'delivery_location_zip', 'weight', 'description')


class CargoCreateSerializer(serializers.ModelSerializer):
    """
    Класс представляет сериализатор для создания нового груза.
    """

    pick_up_location_zip = serializers.SlugRelatedField(
        slug_field='zip_code',
        queryset=Location.objects.all(),
        source='pick_up_location'
    )

    delivery_location_zip = serializers.SlugRelatedField(
        slug_field='zip_code',
        queryset=Location.objects.all(),
        source='delivery_location'
    )

    class Meta:
        """
        Класс для определения метаданных класса сериализатора.
        """

        model = Cargo
        fields = ('pick_up_location_zip', 'delivery_location_zip', 'weight', 'description')


class CargoListSerializer(CargoBaseSerializer):
    """
    Класс представляет сериализатор для списка грузов с информацией о
    количестве ближайших грузовиков.
    """

    nearest_trucks_count = serializers.SerializerMethodField()

    @staticmethod
    def get_nearest_trucks_count(obj: Cargo) -> None:
        """
        Метод для получения количества ближайших машин к месту погрузки груза.

        :param obj: объект модели 'Cargo'.
        """

        trucks = get_trucks_cache()
        location_cargo = (obj.pick_up_location.latitude, obj.pick_up_location.longitude)

        counter = 0
        for truck in trucks:
            location_truck = (truck.current_location.latitude, truck.current_location.longitude)
            distance = geodesic(location_truck, location_cargo).miles
            if distance <= 450:
                counter += 1

        return counter

    class Meta:
        """
        Класс для определения метаданных класса сериализатора.
        """

        model = Cargo
        fields = ('pick_up_location_zip', 'delivery_location_zip', 'nearest_trucks_count')


class CargoRetrieveSerializer(CargoBaseSerializer):
    """
    Класс представляет сериализатор для получения информации о конкретном
    грузе с ближайшими грузовиками.
    """

    nearest_trucks = serializers.SerializerMethodField()

    @staticmethod
    def get_nearest_trucks(obj: Cargo) -> None:
        """
        Метод для получения ближайших машин к месту погрузки груза.

        :param obj: объект модели 'Cargo'.
        """

        trucks = get_trucks_cache()
        location_cargo = (obj.pick_up_location.latitude, obj.pick_up_location.longitude)

        filter_trucks = []
        for truck in trucks:
            location_truck = (truck.current_location.latitude, truck.current_location.longitude)
            distance = geodesic(location_truck, location_cargo).miles
            if distance <= 450:
                filter_trucks.append({'truck_number': truck.number, 'distance': distance})

        return filter_trucks

    class Meta:
        """
        Класс для определения метаданных класса сериализатора.
        """

        model = Cargo
        fields = (
            'pick_up_location_zip',
            'delivery_location_zip',
            'weight',
            'description',
            'nearest_trucks'
        )
