## 1. [Описание](#1)
## 2. [Запуск проекта](#2)
## 3. [Импорт cvs файла в базу данных](#3)
## 4. [Техническая информация](#4)
## 5. [Об авторах(групповой проект)](#5)

---
## 1. Описание <a id=1></a>

Проект YaMDb - библиотека отзывов.
Проект YaMDb собирает отзывы пользователей на произведения. Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.
Произведения делятся на категории, такие как «Книги», «Фильмы», «Музыка». 
Произведению может быть присвоен жанр из списка предустановленных (например, «Сказка», «Рок» или «Артхаус»). 
Добавлять произведения, категории и жанры может только администратор.
Благодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы и ставят произведению оценку в диапазоне от одного до десяти (целое число); из пользовательских оценок формируется усреднённая оценка произведения — рейтинг (целое число). На одно произведение пользователь может оставить только один отзыв.
Пользователи могут оставлять комментарии к отзывам.
Добавлять отзывы, комментарии и ставить оценки могут только аутентифицированные пользователи.

---
## 2. Запуск проекта <a id=2></a>

### Клонировать репозиторий и перейти в него в командной строке:
```
git clone git@github.com:AliceYaroslavtseva/api_yamdb.git
```
### Cоздать и активировать виртуальное окружение:
```
python -m venv venv # Для Windows
python3 -m venv venv # Для Linux и macOS
```
```
source venv/Scripts/activate # Для Windows
source venv/bin/activate # Для Linux и macOS
```
### Установить зависимости из файла requirements.txt:
```
python -m pip install --upgrade pip # Для Windows
python3 -m pip install --upgrade pip # Для Linux и macOS
```
```
pip install -r requirements.txt
```
### Выполнить миграции:
```
python manage.py migrate # Для Windows
python3 manage.py migrate # Для Linux и macOS
```
### Запустить проект:
```
python manage.py runserver # Для Windows
python3 manage.py runserver # Для Linux и macOS
```

---
## 3. Импорт cvs файла в базу данных <a id=3></a>

### Установить приложение:
```
pip install django-import-export
```
### Добавить приложение в settings:
```
# settings.py
INSTALLED_APPS = (
    ...
    'import_export',
)
```
### Применяем collectstatic:
```
$ python manage.py collectstatic
```
### Импорт данных из cvs в БД осуществляется в админ-панеле.

---
## 4. Техническая информация <a id=4></a>

  - Python
  - Django
  - Django Rest Framework
  - GIT
  - SQLite
  - Postman

---
## 5. Об авторах <a id=5></a>

Алиса Ярославцева(тимлид):
```
Telegram: t.me/hellfoxalice
GitHub: github.com/AliceYaroslavtseva
```
Вера Грачева:
```
Telegram: t.me/vveragra
GitHub: github.com/VeraGracheva
```
Николай Кичан:
```
Telegram: t.me/kichannf
GitHub: github.com/kichannf
```
