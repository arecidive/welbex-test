from django.db.models import QuerySet
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from .models import Truck
from .serializers import TruckUpdateSerializer


class TruckViewSet(mixins.UpdateModelMixin,
                   GenericViewSet):
    """
    Класс является ViewSet для обновления машин.
    """

    serializer_class = TruckUpdateSerializer

    def get_queryset(self) -> QuerySet:
        """
        Данный метод возвращает запрос, возвращающий список машин.

        :returns: запрос, возвращающий список машин.
        """

        return Truck.objects.only(
            'number', 'current_location', 'capacity'
        ).select_related('current_location')
