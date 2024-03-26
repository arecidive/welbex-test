import csv

from django.core.management.base import BaseCommand

from ...models import Location


class Command(BaseCommand):
    """
    Класс представляет уоманду для загрузки локаций из файла CSV в базу данных.
    """

    help = 'Загрузка локаций из файла CSV в базу данных.'

    def handle(self, *args, **options) -> None:
        """
        Метод для загрузки локаций из файла CSV в базу данных.
        """

        with open('data/uszips.csv', 'r', encoding='utf-8') as file:
            locations = csv.DictReader(file)

            for row in locations:
                Location.objects.create(
                    zip_code=row['zip'],
                    city=row['city'],
                    state=row['state_name'],
                    latitude=float(row['lat']),
                    longitude=float(row['lng'])
                )

        self.stdout.write(self.style.SUCCESS('Локации успешно загружены в базу данных!'))
