from datetime import datetime

from django.core.exceptions import ValidationError


def validate_year(value):
    """Проверка корректности даты фильма"""
    if value > datetime.now().year:
        raise ValidationError('Увы, будущее еще не наступило')
