# My blog
**ОПИСАНИЕ:**

My blog - это учебный Pet-проект, в рамках изучения чистого Django, по 
ведению блога, созданию постов и комментариев. В проекте реализован следующий 
функционал:
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

1. Создай контейнер проекта (директорию, папку) и перейди в нее:
```
mkdir MyBlog
cd MyBlog
```

2. Клонируй проект:
```
git clone git@github.com:smaspb17/my_blog.git
```
3. Создай виртуальное окружение для проекта. Это позволит изолировать 
   проект от системных зависимостей и установленных библиотек. Для создания виртуального окружения используй команду:
```
python -m venv venv
```
4. Активируй виртуальное окружение командой:
```
source venv/Scripts/activate
```
5. Перейди в пакет проекта и установи необходимые зависимости:
```
cd my_blog/
pip install -r requirements.txt
```
6. При необходимости обнови пакетный менеджер pip:
``` 
python.exe -m pip install --upgrade pip
```
7. Создай пользователя и базу данных используя оболочку psql
```
psql -U postgres
CREATE USER blog WITH PASSWORD 'your_password';
CREATE DATABASE blog OWNER blog ENCODING 'UTF8';
```
8. Открой файл конфигурации settings.py и внеси строки для базы данных:
```
"ENGINE": "django.db.backends.postgresql",
"NAME": 'blog',
"USER": 'blog',
"PASSWORD": 'your_password',
```
9. Перейди в пакет конфигурации и выполни миграции, там находится файл 
   manage.py:
```
cd my_blog/
python manage.py makemigrations
python manage.py migrate
```
10. Создай приложение в google-аккаунте и заполни настройки для 
    отправки электронных писем по smtp-протоколу:
```
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = "your_host_user"
EMAIL_HOST_PASSWORD = "your_host_paswword"
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
SERVER_EMAIL = EMAIL_HOST_USER
EMAIL_ADMIN = EMAIL_HOST_USER
```
11. Создай суперпользователя:
```
python manage.py createsuperuser
```
12. Запусти проект на локальном сервере:
```
python manage.py runserver
```
13. Перейди по ссылке в браузере:
```
http://127.0.0.1:8000/blog/
``` 
Теперь ты можешь использовать проект на своём компьютере. Если ты хочешь остановить проект, нажми Ctrl+C в терминале, а затем деактивируй виртуальное окружение командой:
```
deactivate
```

**АВТОР:** Шайбаков Марат


**ЛИЦЕНЗИЯ:** Apache License 2.0


**КОНТАКТЫ:** smaspb17@yandex.ru


