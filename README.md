# BraniacLMS
Setting up for Django project with Pyenv and Poetry

ДЗ 4:
заполнила БД след. способами - 
news - из терминала (ipython)
course - через команду наполнения  python manage.py fill_courses
lesson - загрузка данных из фикстуры  python manage.py loaddata 003_lessons.json
попыталась заполнить coursesteacher через seeding, но не получилось,
ошибка django.db.utils.OperationalError: no such table: seeding_seeding.
Почему он ищет таблицу seeding_seeding? Как заполнить данными таблицу coursesteacher?
Не очень поняла, как это работает.
сделала python manage.py seeding create - создался фаил 0001_auto_name.py
что должно быть в функции seeding? Сначала я написала туда код, как в файле fill_teachers.py - no such table: seeding_seeding,
потом только первую строку с конкретными данными - как вы можете видеть - та же  ошибка.
Честно говоря, я думала, что ваш код заполняет таблицу фейковыми данными. 
Объясните, пожалуйста, как это работает?
