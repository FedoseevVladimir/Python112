папка: first-app

в терминале:
cd first-app

django-admin startproject drfsite

python manage.py runserver

python manage.py startapp telebot

папка templates
    home.html

python manage.py collectstatic - подключает static файлы


python manage.py makemigrations
python manage.py migrate - применяет миграции моделей

python manage.py createsuperuser - создать пользователя админ
python manage.py changepassword admin - если нужно изменить пароль


python manage.py dumpdata products.ProductCategory > category.json
python manage.py dumpdata products.Product > goods.json


models.CASCADE - если пользователь будет удален, с ним удалятся и все задачи
models.PROTECTED - запрещает удалять пользователя пока у него есть задачи
models.SET_NULL - задачи остануться в базе, даже при удалении пользователя но значение в поле задачи изменится на None
models.SET_DEFAULT - задачи остануться в базе, даже при удалении пользователя но значение в поле задачи изменится на значение по умолчанию

ЮТУБ ЕЛЕНЫ С НАШИМИ ЛЕКЦИЯМИ
https://www.youtube.com/playlist?list=PL-Hq_KrfJ31U3vlc1XXUlLI6n2GC7IhPP
https://github.com/Helen-prog/Python112

регистрация пользователя - 06.07.2022, 102 пара, 112 пара тоже регистрация но другая
Занятие 58 - выкладываем в интернет (создаем репозиторий) 115 пара
занятие 59 - слайд
занятие 23.08.2022 создавали телеграмм бота
пагинатор - 31.08.2022 занятие
сохранение базы данных в csv файл - 31.08.2022 занятие

110 пара 1:15:00 миксин для перевода если не зареган можно
переводить по клику на мои курсы на окно регистрации

111 пара пагинатор для создания страниц если много курсов
128-129 пара создание корзины и привязка к юзеру
136 пара добавление api на сайт для постинга элементов
sandme231123_bot
https://api.telegram.org/bot5465955700:AAHGdwrYAQaOKh0ZQ2oLy62wekxqFmmvGEg/sendMessage?chat_id=-821210673&text=test

"Montserrat" - шрифт

https://skillsupschool.ru/intensives/intensiv-2dgrafika-msc/ - как сделать такой фон?


134 пара rest framework (занятие 67)
https://github.com/FedoseevVladimir/diplom_work
{
"title": "Новость 2",
"content": "Содержание новости 2",
"category_id": 2
}