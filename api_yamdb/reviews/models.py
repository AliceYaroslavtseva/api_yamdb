from django.db import models

from .validators import validate_year


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
