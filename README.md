# api_yamdb

![Git-Hub Actions](https://github.com/alien-guest/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

## Описание

Яндекс Практикум. Спринт 16. Api для проекта Yamdb

## Как запустить проект локально

1. Клонировать репозиторий и перейти в него в командной строке:

   ```
   git clone git@github.com:alien-guest/yamdb_final.git
   ```

   ```
   cd yamdb_final/
   ```

2. Запустить Docker-compose:

   ```
   docker-compose up -d
   ```

3. Поочередно ввести 4 команды:

   ```
   docker-compose exec web python manage.py migrate
   docker-compose exec web python manage.py collectstatic --no-input
   docker-compose exec web python manage.py createsuperuser
   docker-compose exec web python manage.py loaddata fixtures.json
   
   ```

4. По окончании локальной работы остновить и удалить контейнеры:

   ```
   docker-compose down
   ```

## Ресурсы

- Документация проекта
http://158.160.18.242/redoc/

- Прямая ссылка в админку для удобства ревью
http://158.160.18.242/admin/

## Автор проекта

Антон Гуляев
