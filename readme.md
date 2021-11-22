# Пример сайта на Flask

## Запуск сервера для разработки

В PowerShell:

* `venv\scripts\activate.ps1`
* `$ENV:FLASK_APP = "app"`
* `flask run`

В командной строке Windows:

* `venv\scripts\activate.bat`
* `set FLASK_APP=app`
* `flask run`

В Git Bash (Windows):

* `. venv/scripts/activate`
* `export FLASK_APP=app`
* `flask run`


## Миграция базы данных

Инициализация библиотеки миграции данных (это нужно сделать только один раз):

`flask db init`

При каждом изменении в структуре базы данных нужно:

1. `flask db migrate -m "Comment"` - создание скрипта миграции данных
2. `flask db upgrade` - применение скрипта миграции данных
