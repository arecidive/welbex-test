from random import choice

from celery import shared_task

from location.models import Location

from .models import Truck


@shared_task
def update_truck_locations() -> None:
    """
    Асинхронная Celery-задача для обновления локации машин. Задача выполняет обновление поля 'location'
    для машины, выбирая случайную локацию.
    """

    location_ids = list(Location.objects.all())

    trucks = list(Truck.objects.all())
    for truck in trucks:
        truck.current_location = choice(location_ids)

    Truck.objects.bulk_update(trucks, ['current_location'])
