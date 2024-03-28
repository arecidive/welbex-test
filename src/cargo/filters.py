from django.db.models import QuerySet
from geopy.distance import geodesic
from rest_framework import filters
from rest_framework.request import Request

from truck.models import Truck

from .models import Cargo


class CargoFilterBackend(filters.BaseFilterBackend):
    """
    Класс представляет фильтр, который фильтрует список грузов по весу и/или ближайшему грузовику.
    """

    def filter_queryset(self, request: Request, queryset: QuerySet, view) -> list[Cargo] | QuerySet:
        """
        Фильтрует список грузов на основе параметров запроса.

        :param request: запрос клиента.
        :param queryset: набор данных грузов для фильтрации.
        :param view: представление, к которому применяется фильтр.

        :returns: отфильтрованный список грузов.
        """

        weight = request.query_params.get('weight')
        truck_number = request.query_params.get('truck_number')

        if weight:
            queryset = queryset.filter(weight=weight)

        if truck_number:
            try:
                truck = Truck.objects.select_related('current_location').get(number=truck_number)

                truck_location = (truck.current_location.latitude, truck.current_location.longitude)

                filtered_cargos = []
                for cargo in queryset:
                    cargo_location = (cargo.pick_up_location.latitude, cargo.pick_up_location.longitude)
                    distance = geodesic(truck_location, cargo_location).miles
                    if distance <= 450:
                        filtered_cargos.append(cargo)

                return filtered_cargos

            except Truck.DoesNotExist:
                return queryset

        return queryset
