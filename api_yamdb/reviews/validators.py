from django.core.exceptions import ValidationError
from datetime import datetime


def validate_year(value):
    """Проверка корректности даты фильма"""
    if value > datetime.now().year:
        raise ValidationError('Увы, будущее еще не наступило')
    if value < 1895:
        raise ValidationError(
            f'Кажется, в {value} году еще не было фильмов. '
            f'Первый фильм был снят в 1895 году.'
        )
