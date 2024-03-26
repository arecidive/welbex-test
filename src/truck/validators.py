import re

from django.core.exceptions import ValidationError


def validate_truck_number(value: str) -> None:
    """
    Функция является валидатором для номера машины. Проверяет, соответствует ли номер
    машины заданному формату. Номер машины должен быть в формате: цифра от 1000 до 9999 + случайная
    заглавная буква английского алфавита в конце.

    :param value: номер машины для проверки.
    :raises ValidationError: если номер машины не соответствует формату.
    """

    if not re.match(r'^[1-9]\d{3}[A-Z]$', value):
        raise ValidationError(
            'Номер машины должен быть в формате: от 1000 до 9999 + случайная '
            'заглавная буква английского алфавита в конце.',
            code='invalid_truck_number'
        )
