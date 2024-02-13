## Описание

Приложение может получать список торговых точек. Пример GET запроса:

http://127.0.0.1:8000/api/stores/phone_number/

А также выполнить посещение в торговую точку POST:

http://127.0.0.1:8000/api/visits/create/phone_number/

## Запуск

1. Клонируем репозиторий на локальный компьютер 

```
git clone https://github.com/Petro2561/Factory_test.git
```

2. Создаем .env файл в корневой директории

```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=<Your_password>
DB_HOST=foodgram-db
DB_PORT=5432
```

3. Запускаем контейнеры (Предполагается, что у вас установлен докер)
```
docker-compose up
```
4. Создаем суперюзера
```
docker exec -it <id container or name> createsuperuser
```

Приложение готово к работе!

## Использованные технологии:
- Python 3.10
- Django 4.2.6
- Django REST framework 3.14
- Docker
- Postgres

