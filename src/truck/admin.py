from django.contrib import admin

from .models import Truck


@admin.register(Truck)
class TruckAdmin(admin.ModelAdmin):
    """
    Административная конфигурация для модели 'Truck'.
    """

    list_display = ('number', 'current_location', 'capacity')
    raw_id_fields = ('current_location',)
