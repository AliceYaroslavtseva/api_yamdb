from django.core.exceptions import ValidationError
from datetime import datetime


def validate_year(value):
    """Проверка корректности даты фильма"""
    if value > datetime.now().year:
        raise ValidationError('Увы, будущее еще не наступило')
