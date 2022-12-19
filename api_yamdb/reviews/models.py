from django.contrib.auth.models import AbstractUser
from django.core.validators import (MaxValueValidator, MinValueValidator,
                                    RegexValidator)
from django.db import models

from api_yamdb.settings import ROLE_CHOICES

from .validators import validate_year


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


class Category(models.Model):

    name = models.CharField('Категория', max_length=256)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Genre(models.Model):

    name = models.CharField('Жанр', max_length=256)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Title(models.Model):

    name = models.CharField('Название', max_length=256)
    year = models.IntegerField('Год выпуска', validators=(validate_year, ))
    description = models.TextField('Описание', blank=True, null=True)
    genre = models.ManyToManyField(
        Genre,
        verbose_name='Жанр',
        related_name='title',
        through='GenreTitle',
    )
    category = models.ForeignKey(
        Category,
        verbose_name='Категория',
        related_name='title',
        blank=False, null=True,
        on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.name


class GenreTitle(models.Model):

    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    title = models.ForeignKey(Title, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.genre}{self.title}'


class Review(models.Model):
    title = models.ForeignKey(
        Title,
        verbose_name='Произведение',
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    text = models.TextField(
        verbose_name='Отзыв',
    )
    author = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    score = models.IntegerField(
        verbose_name='Рейтинг',
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10)
        ]
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True,
        db_index=True
    )

    class Meta:
        ordering = ['pub_date']


class Comment(models.Model):
    review = models.ForeignKey(
        Review,
        verbose_name='Отзыв',
        on_delete=models.CASCADE,
        related_name='comments'
    )
    text = models.TextField(
        verbose_name='Коментарий',
    )
    author = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.CASCADE,
        related_name='comments'
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True,
        db_index=True
    )

    class Meta:
        ordering = ['pub_date']
