from rest_framework import serializers

from location.models import Location

from .models import Truck


class TruckUpdateSerializer(serializers.ModelSerializer):
    """
    Класс представляет сериализатор для обновления информации о машине.
    """

    current_location_zip = serializers.SlugRelatedField(
        slug_field='zip_code',
        queryset=Location.objects.all(),
        source='current_location'
    )

    class Meta:
        """
        Класс для определения метаданных класса сериализатора.
        """

        model = Truck
        fields = ('number', 'current_location_zip', 'capacity')
        read_only_fields = ('number', 'capacity')
