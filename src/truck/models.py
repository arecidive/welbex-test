from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from location.models import Location

from .validators import validate_truck_number


class Truck(models.Model):
    """
    Модель для хранения информации о машине.
    """

    number = models.CharField(
        max_length=5,
        unique=True,
        validators=[validate_truck_number],
        verbose_name='Номер машины'
    )

    current_location = models.ForeignKey(
        to=Location,
        on_delete=models.PROTECT,
        verbose_name='Текущая локация'
    )

    capacity = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1, message='Грузоподъемность должна быть не меньше 1!'),
            MaxValueValidator(1000, message='Грузоподъемность должна быть не больше 1000!')
        ],
        verbose_name='Грузоподъемность'
    )

    def __str__(self):
        """
        Метод возвращает строковое представление объекта, содержащее номер машины.

        :returns: строковое представление объекта.
        """

        return f'{self.number}'

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'
