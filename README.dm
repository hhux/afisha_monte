Создать и запустить прод контейнер
docker-compose -f docker-compose.prod.yml up -d --build

сделать миграции/собрать статику в контейнере можно двумя способами:
1) использовать баш файл bash debug.sh
2) сделать миграции/собрать статику вручную
    docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
    docker-compose -f docker-compose.prod.yml exec web python manage.py makemigrations --noinput
    docker-compose -f docker-compose.prod.yml exec web python manage.py makemigrations afisha_monte
    docker-compose -f docker-compose.prod.yml exec web python manage.py migrate afisha_monte
    docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear


Создать суперпользователя в контейнере
docker exec -it <айди контейнера> python manage.py createsuperuser

Зайти внутрь контейнера
docker exec -it <айди контейнера> bash


Постгрес для создания/удаления базы:
1) Провалиться в постгрес psql postgres -U afisha_monte
2) Создать/Удалить базу данных CREATE DATABASE/DELETE DATABASE
