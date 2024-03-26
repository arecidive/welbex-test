from django.db import models

from location.models import Location


class Truck(models.Model):
    """
    Модель для хранения информации о машине.
    """

    number = models.CharField(max_length=5, unique=True, verbose_name='Номер машины')

    current_location = models.ForeignKey(
        to=Location,
        on_delete=models.PROTECT,
        verbose_name='Текущая локация'
    )

    capacity = models.IntegerField(verbose_name='Грузоподъемность')

    def __str__(self):
        """
        Метод возвращает строковое представление объекта, содержащее номер машины.

        :returns: строковое представление объекта.
        """

        return f'{self.number}'

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'
