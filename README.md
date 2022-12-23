# api_yamdb
## Проект YaMDb собирает отзывы пользователей на произведения.
## Приложение работает через api
## Документацию проекта можно посмотреть по адресу:
```
http://127.0.0.1:8000/redoc/
```

### Как запустить проект:
#### Клонировать репозиторий и перейти в него в командной строке:
```
git clone git@github.com:AliceYaroslavtseva/api_yamdb.git
cd api_yamdb
```
#### Cоздать и активировать виртуальное окружение:
```
python3 -m venv env
source env/bin/activate
или
. venv/Scripts/activate
```
#### Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```
### Выполнить миграции:
```
python3 manage.py migrate
```
### Запустить проект:
```
python3 manage.py runserver
```

### Импорт cvs файла в базу данных.
### Установить приложение.
```
pip install django-import-export
```
### Добавить приложение в settings
```
# settings.py
INSTALLED_APPS = (
    ...
    'import_export',
)
```
### Применяем collectstatic
```
$ python manage.py collectstatic
```
### Импорт данных из cvs в БД осуществляется в админ-панеле.
