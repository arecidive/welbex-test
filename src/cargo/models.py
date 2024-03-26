from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from location.models import Location


class Cargo(models.Model):
    """
    Модель для хранения информации о грузе.
    """

    pick_up_location = models.ForeignKey(
        to=Location,
        related_name='pick_up_cargo',
        on_delete=models.PROTECT,
        verbose_name='Локация нахождения груза'
    )

    delivery_location = models.ForeignKey(
        to=Location,
        related_name='delivery_cargo',
        on_delete=models.PROTECT,
        verbose_name='Локация доставки груза'
    )

    weight = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1, message='Вес груза должен быть не меньше 1!'),
            MaxValueValidator(1000, message='Вес груза должна быть не больше 1000!')
        ],
        verbose_name='Вес груза'
    )

    description = models.TextField(verbose_name='Описание груза')

    def __str__(self):
        """
        Метод возвращает строковое представление объекта, содержащее информацию о грузе.

        :returns: строковое представление объекта.
        """

        return f'{self.pick_up_location} -> {self.delivery_location}'

    class Meta:
        """
        Класс для определения метаданных модели.
        """

        verbose_name = 'Груз'
        verbose_name_plural = 'Грузы'
