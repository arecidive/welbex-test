from django.contrib import admin

from .models import Cargo


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    """
    Административная конфигурация для модели 'Cargo'.
    """

    list_display = ('pick_up_location', 'delivery_location', 'weight', 'description')
    raw_id_fields = ('pick_up_location', 'delivery_location')
