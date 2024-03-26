from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet

from . import serializers
from .models import Cargo


class CargoViewSet(ModelViewSet):
    """
    Класс является ViewSet для управления грузами.
    """

    def get_queryset(self):
        """
        Данный метод возвращает запрос, возвращающий список устройств, принадлежащих
        текущему пользователю.

        :returns: запрос, возвращающий список устройств.
        """

        return Cargo.objects.only(
            'pick_up_location', 'delivery_location', 'weight', 'description'
        ).select_related('pick_up_location', 'delivery_location')

    def get_serializer_class(self) -> ModelSerializer:
        """
        Метод возвращает класс сериализатора в зависимости от выполняемого действия.

        :returns: класс сериализатора.
        """

        if self.action == 'create':
            return serializers.CargoCreateSerializer
        if self.action == 'list':
            return serializers.CargoListSerializer
        if self.action == 'retrieve':
            return serializers.CargoRetrieveSerializer
        return serializers.CargoUpdateSerializer
