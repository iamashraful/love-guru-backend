# Money Tacker API

> This repository only represents the API part. The client app is available under https://github.com/iamashraful/money-tracker-client

### How to run locally or ready for production?
* Clone first [ You may fork then clone ]
* Copy `config/db_config.py.SAMPLE` and make your own `db_config.py` and update the file according to your own database config
* Create Virtualenv `virtualenv -p python3 /path/to/env/venv`
* Then create database table with `python manage.py migrate`
* Create user for access `python manage.py create_profile`
* Finally `python manage.py runserver`

*That's it for now :)*
