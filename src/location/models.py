from django.db import models


class Location(models.Model):
    """
    Модель для хранения информации о локации.
    """

    city = models.CharField(max_length=100, verbose_name='Город')
    state = models.CharField(max_length=100, verbose_name='Штат')
    zip_code = models.CharField(max_length=10, verbose_name='Почтовый индекс')
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долгота')

    def __str__(self):
        """
        Метод возвращает строковое представление объекта, содержащее название
        города, штата, широту и долготу.

        :returns: строковое представление объекта.
        """

        return f'{self.city} - {self.state} ({self.latitude}, {self.longitude})'

    class Meta:
        """
        Класс для определения метаданных модели.
        """

        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'
