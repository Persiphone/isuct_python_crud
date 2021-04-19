## Устанавливаем Flask
    pip install Flask

## Устанавливаем SQLAlchemy
    pip install SQLAlchemy

## Docker
После того как установили проект, необходимо установить на свой компьютер docker и выполнить комманду:
    
    docker run --name mydatabase -e POSTGRES_DB=crud_db -e POSTGRES_USER=crud_user_db -e POSTGRES_PASSWORD=crud_user_password -p 5432:5432 -d postgres

## Миграции
Устанавливаем пакет Flask-Script

    pip install Flask-Script

Устанавливаем миграции

    py migrations.py db init
    py migrations.py db migrate
    py migrations.py db upgrade

## Запускаем проект
В корневой папке (там где лежит файл index.py) выполняем комманду:

    py index.py - для Windows
    python3 index.py - для Linux