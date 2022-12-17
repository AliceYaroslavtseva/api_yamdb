from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

from api_yamdb.settings import ROLE_CHOICES


class User(AbstractUser):
    username = models.CharField(
        'Логин',
        max_length=150,
        unique=True,
        help_text='Nickname',
        validators=[
            RegexValidator(
                regex=r'^[\w.@+-]+',
                message=('Nickname должен содержать буквы,'
                         'цифры и символы @.+-_')
            )
        ]
    )
    password = models.CharField(
        'Пароль',
        max_length=150,
        blank=True,
        help_text='Пароль',
    )
    email = models.EmailField(
        'e-mail',
        max_length=254,
        unique=True,
        help_text='Электронная почта',
    )
    first_name = models.CharField(
        'Имя',
        max_length=150,
        blank=True,
        help_text='Имя',
    )
    last_name = models.CharField(
        'Фамилия',
        max_length=150,
        blank=True,
        help_text='Фамилия',
    )
    bio = models.TextField(
        'Биография',
        blank=True,
        help_text='Биография',
    )
    role = models.TextField(
        'Роль',
        choices=ROLE_CHOICES,
        default='user',
        help_text='Роль пользователя',
    )

    class Meta:
        ordering = ('username',)

    def __str__(self) -> str:
        return self.username
