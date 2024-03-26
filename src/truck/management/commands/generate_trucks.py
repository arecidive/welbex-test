import random
import string

from django.core.management.base import BaseCommand, CommandParser

from location.models import Location

from ...models import Truck


class Command(BaseCommand):
    """
    Класс представляет команду управления для генерации случайных машин
    и их добавления в базу данных.
    """

    help = 'Создает случайные машины и добавляет их в базу данных.'

    def add_arguments(self, parser: CommandParser) -> None:
        """
        Метод добавляет аргументы командной строки.

        :param parser: парсер аргументов.
        """

        parser.add_argument('count', type=int, help='Количество машин для генерации.')

    def handle(self, *args, **options) -> None:
        """
        Метод обрабатывает выполнение команды, генерирует заданное количество машин и добавляет их
        в базу данных.
        """

        count = options['count']
        for _ in range(count):
            number = ''.join(random.choices(string.digits, k=4)) + random.choice(string.ascii_uppercase)
            capacity = random.randint(1, 1000)
            location = Location.objects.order_by('?').first()
            Truck.objects.create(number=number, current_location=location, capacity=capacity)

        self.stdout.write(
            self.style.SUCCESS(f'{count} случайных машин успешно созданы и добавлены в базу данных!')
        )
