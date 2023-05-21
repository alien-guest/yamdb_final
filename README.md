# api_yamdb

[![Python](https://img.shields.io/badge/-Python-464641?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-464646?style=flat-square&logo=django)](https://www.djangoproject.com/)
[![Pytest](https://img.shields.io/badge/Pytest-464646?style=flat-square&logo=pytest)](https://docs.pytest.org/en/6.2.x/)
[![Postman](https://img.shields.io/badge/Postman-464646?style=flat-square&logo=postman)](https://www.postman.com/)

![Git-Hub Actions](https://github.com/alien-guest/yamdb_final/actions/workflows/yamdb_workflow/badge.svg)
## Описание

Яндекс Практикум. Спринт 16. Api для проекта Yamdb

## Как запустить проект

1. Клонировать репозиторий и перейти в него в командной строке:

   ```
   git clone git@github.com:alien-guest/infra_sp2.git
   ```

   ```
   cd infra_sp2/
   ```

2. Запустить Docker-compose:

   ```
   docker-compose up
   ```

3. Поочередно ввести 4 команды:

   ```
   docker-compose exec web python manage.py migrate
   docker-compose exec web python manage.py createsuperuser
   docker-compose exec web python manage.py collectstatic --no-input
   docker-compose exec web python manage.py loaddata fixtures.json
   ```

## Шаблон наполнения env-файла

   ```
   DB_ENGINE=example # указываем, что работаем с postgresql
   DB_NAME=example # имя базы данных
   POSTGRES_USER=example # логин для подключения к базе данных
   POSTGRES_PASSWORD=example # пароль для подключения к БД (установите свой)
   DB_HOST=example # название сервиса (контейнера)
   DB_PORT=example # порт для подключения к БД   
   ```
