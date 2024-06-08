<a id="anchor"></a>

<div align=center>

# Тестовое задание

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)

</div>

## Описание тестового задания

```
Тестовое задание на позицию Backend-разработчик на языке Python.
Требуется разработать API-сервис для получения данных о первых 10
объявлениях по ссылке:
https://www.farpost.ru/vladivostok/service/construction/guard/+/Системы+видеонаблюдения/ .
Для решения задачи необходимо:
    1. Разработать модели при помощи фреймворка Django/FastAPI со
    следующими полями:
        - заголовок объявления;
        - id объявления;
        - автор объявления;
        - количество просмотров объявления;
        - позиция, на которой стоит объявление.
    Данные могут быть добавлены в БД вручную или любым удобным для
    вас способом.
    2. Разработать методы API для обращения к данным моделям.
    Запрос к API должен иметь параметр ID. При обращении, API должен
    возвращать информации об объявлении с ID, переданным в запросе, в формате JSON.
Требования к реализации API:
    1. При разработке должен быть использован язык Python и
    фреймворк Django/FAST Api.
    2. В качестве результата должен быть предоставлен репозиторий
    на GitHub;
    3. Сервис должен использовать принципы ООП.
    Дополнительные требования, не обязательны к выполнению,
    но будут являться большим плюсом:
    1. Реализована система регистрации и входа (верификации
    аккаунта) для подключения к API (без функционала смены и/или
    восстановления пароля);
Все обращения к базе данных должны быть реализованы при помощи
ORM запросов.
```

### Технологии

Python 3.10.11

Django 4.2
Django REST Framework 3.15.1

Database SQLite

<details>
<summary>
<h4>Запуск проекта</h4>
</summary>

<br>

```
склонировать проект:
git clone git@github.com:JustLight1/testovoe-it-solutions.git
```

- При первом запуске для функционирования проекта обязательно установить виртуальное окружение и установить зависимости:

```
python -m venv venv

source venv/Scripts/activate

python -m pip install --upgrade pip
```

- Установите зависимости из файла requirements.txt

```
pip install -r requirements.txt
```

- Для запуска сервера из папки src с файлом manage.py выполните команду:

```
python manage.py runserver
```

Для доступа в админку использовать данные:

```
username: admin
password: 1
```

**API**

Список объявлений осуществляется по адресу:

```
http://127.0.0.1:8000/api/posts/
```

Запрос к конкретному объявлению осуществляется по адресу:

```
http://127.0.0.1:8000/api/post/{id}/
```

<details>
<summary>
<h4>Шаблон наполнения env-файла</h4>
</summary>

<br>

```env
  DEBUG=True/False
  SECRET_KEY=''
```

</details>

## Контакты:

**Форов Александр**

[![Telegram Badge](https://img.shields.io/badge/-Light_88-blue?style=social&logo=telegram&link=https://t.me/Light_88)](https://t.me/Light_88) [![Gmail Badge](https://img.shields.io/badge/forov.py@gmail.com-c14438?style=flat&logo=Gmail&logoColor=white&link=mailto:forov.py@gmail.com)](mailto:forov.py@gmail.com)
