# api_yamdb
api_yamdb

ля
ля
ля
ля
ля
ля
## Импорт базы данных.
### Установка приложения
```
pip install django-import-export
```
### Добавляем приложении в settings
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