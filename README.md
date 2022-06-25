# final-exem
Для запуска провекта создайте виртуальное окружение
``` 
python -m venv venv
```
Далее запустите его
```
venv/Scripts/activate
```
или
```
venv/bin/activate
```
И установите библиотеки для работы приложения
``` 
pip install -r requirements.txt

```

Отлично, теперь переходим на конфигурацию данных PostgreSQL
Создайте файл .env в директории ```/source```
Далее заполните поля по примерам из .env.sample
Затем примините миграции
```
./manage.py migrate
```
И загрузите фикстуры
```
./manage.py loaddata fixtures/auth.json
./manage.py loaddata fixtures/dump.json
```
И наконец запустите сервер
```
./manage.py runserver
```
