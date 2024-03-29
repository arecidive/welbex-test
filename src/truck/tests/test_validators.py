from contextlib import nullcontext as does_not_raise

import pytest
from django.core.exceptions import ValidationError

from truck.validators import validate_truck_number


class TestValidateTruckNumber:
    """
    Класс представляет тесты для модели 'validate_truck_number'.
    """

    @pytest.mark.parametrize(
        'number, expectation',
        [
            ('123', pytest.raises(ValidationError)),
            ('123456', pytest.raises(ValidationError)),
            ('ABCD', pytest.raises(ValidationError)),
            ('1TEST', pytest.raises(ValidationError)),
            ('haha', pytest.raises(ValidationError)),
            ('A1A1A1', pytest.raises(ValidationError)),
            ('1000A', does_not_raise()),
            ('9999Z', does_not_raise()),
            ('5678B', does_not_raise()),
            ('1234M', does_not_raise()),
            ('2345X', does_not_raise())
        ]
    )
    def test_validate_truck_number(self, number: str, expectation) -> None:
        """
        Тест для проверки валидатора 'validate_truck_number'. Проверяет входную строку
        на соответствие валидации функции 'validate_truck_number'. Если 'expectation' равен
        'does_not_raise()', то ожидается успешное прохождение теста без вызова исключения. Если
        'expectation' равен 'pytest.raises(ValidationError)', то ожидается вызов исключения 'ValidationError'.

        :param test_input: тестируемая строка.
        :param expectation: ожидание результата теста, может быть does_not_raise() для валидных входных данных
        или pytest.raises(ValidationError) для невалидных входных данных.
        """

        with expectation:
            validate_truck_number(number)
