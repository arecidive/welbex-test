from .. import serializers
from ..views import CargoViewSet


class TestCargoViewSet:
    """
    Класс для тестирования ViewSet 'CargoViewSet'.
    """

    def test_get_serializer_class(self) -> None:
        """
        Тест проверяет метод 'get_serializer_class' (метод 'get_serializer_class' возвращает правильный
        класс сериализатора в зависимости от действия).
        """

        view_set = CargoViewSet()

        view_set.action = 'create'
        assert view_set.get_serializer_class() == serializers.CargoCreateSerializer

        view_set.action = 'list'
        assert view_set.get_serializer_class() == serializers.CargoListSerializer

        view_set.action = 'retrieve'
        assert view_set.get_serializer_class() == serializers.CargoRetrieveSerializer

        view_set.action = 'update'
        assert view_set.get_serializer_class() == serializers.CargoUpdateSerializer

        view_set.action = 'destroy'
        assert view_set.get_serializer_class() == serializers.CargoUpdateSerializer
