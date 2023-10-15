News_Portal
This is a django python project in which we create a website with the publication of news written by individual authors.

Django shell
to start project
python manage.py runserver

to create admin user
python manage.py createsuperuser

to create db
python manage.py migrate

to make migration
python manage.py makemigrations

to change migrations
python manage.py makemigrations --empty python manage.py makemigrations --update python manage.py makemigrations


Applications have been created to implement the site: - ### ***accounts*** - [link to Accounts models.py](./News_Portal/Accounts/models.py) - ### *news* ```some comand```
module D 5.8

1-Добавьте форму регистрации на сайте с возможностью зарегистрироваться с помощью почты и пароля или через Yandex-аккаунт. Для этого используйте пакет django-allauth. После того как пользователь войдёт, его должно перенаправить на страницу с новостями.

2-Настройте проверки у представлений создания и редактирования новостей и статей. Создайте группу authors, выдайте ей права на создание и изменение новых записей в разделах «Статьи» и «Новости».

3-Проверьте работу прав.
