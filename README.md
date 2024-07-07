# My blog
**ОПИСАНИЕ:**

My blog - это учебный Pet-проект по ведению блога, созданию постов 
и комментариев, в рамках изучения чистого Django. В проекте реализован
следующий функционал:
- модели, представления, пути и шаблоны постов и комментариев
- система тегирования django-taggit
- рекомендации схожих постов по тегам (сложный QuerySet запрос)
- кастомный менеджер модели published
- кастомные шаблонные теги и фильтр (markdown)
- пагинация списка постов в функции и классе представлении
- отправка постов по электронной почте через smtp-сервер Google
- карта сайта и новостная RSS-лента
- полнотекстовый поисковый механизм PostgreSQL (классы SearchVector, SearchQuery, SearchRank, TrigramSimilarity)

**СТЕК ТЕХНОЛОГИЙ:**
Python 3.12, Django 4.2.7, Postgresql 15   

**ЛОКАЛЬНАЯ УСТАНОВКА (для Windows):**

1. Клонируй проект и перейди в него:
```shell
git clone git@github.com:smaspb17/my_blog.git
сd my_blog
```
2. Создай виртуальное окружение для проекта. Это позволит изолировать 
проект от системных зависимостей и установленных библиотек:
```shell
python -m venv venv
```
3. Активируй виртуальное окружение командой:
```shell
venv/Scripts/activate
```
4. Установи необходимые зависимости:
```shell
pip install -r requirements.txt
```
5. При необходимости обнови пакетный менеджер pip:
```shell
python.exe -m pip install --upgrade pip
```
6. Создай пользователя и базу данных используя оболочку psql:
```
psql -U postgres
CREATE USER blog WITH PASSWORD 'your_password';
CREATE DATABASE blog OWNER blog ENCODING 'UTF8';
```
7. Создай файл .env (в контейнере проекта), а также приложение в любом 
smtp-сервисе, например в Google (https://myaccount.google.com), и 
заполни его переменными, указанными в файле example.env.

8. Перейди в пакет проекта (`my_blog/my_blog`, там где находится файл 
manage.py) и выполни миграции:
```shell
cd my_blog/
python manage.py makemigrations
python manage.py migrate
```
9. Создай суперпользователя:
```shell
python manage.py createsuperuser
```
10. Запусти проект на локальном сервере:
```shell
python manage.py runserver
```
11. Перейди по ссылке в браузере:
```
http://127.0.0.1:8000/blog/
``` 
Теперь ты можешь использовать проект на своём компьютере. Если ты хочешь остановить проект, нажми Ctrl+C в терминале, а затем деактивируй виртуальное окружение командой:
```shell
deactivate
```

**АВТОР:** Шайбаков Марат


**ЛИЦЕНЗИЯ:** Apache License 2.0


**КОНТАКТЫ:** smaspb17@yandex.ru


