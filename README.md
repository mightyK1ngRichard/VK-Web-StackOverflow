# Домашнее задание №3

Для запуска БД надо поднять докер, запустить миграции, заполнить бд
```swift
docker-compose up -d
python manage.py migrate
python manage.py fill_db [ratio]     
```
